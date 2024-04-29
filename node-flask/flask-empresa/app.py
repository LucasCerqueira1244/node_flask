from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1/empresa'
db = SQLAlchemy(app)

# Definição dos modelos
class Setor(db.Model):
    id_setor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    setor = db.Column(db.String(80), nullable=False)

    funcionarios = db.relationship('Funcionario', backref='setor', lazy=True)

    def __str__(self):
        return f'Setor {self.setor}'

class Funcionario(db.Model):
    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primeiro_nome = db.Column(db.String(80), nullable=False)
    sobrenome = db.Column(db.String(80), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)

    id_setor = db.Column(db.Integer, db.ForeignKey('setor.id_setor'), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id_cargo'), nullable=False)

    def __str__(self):
        return f'{self.primeiro_nome} {self.sobrenome}'

class Cargo(db.Model):
    id_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cargo = db.Column(db.String(80), nullable=False)

    funcionarios = db.relationship('Funcionario', backref='cargo', lazy=True)

    def __str__(self):
        return f'Cargo {self.cargo}'

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota para a página inicial
@app.route('/empresa')
def index():
    funcionarios = Funcionario.query.all()
    return render_template('index.html', funcionarios=funcionarios)

# Rota para cadastrar funcionários
@app.route('/cadastrar_funcionario', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        setor_id = request.form['setor']
        cargo_id = request.form['cargo']
        
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']
        data_admissao = request.form['data_admissao']

        novo_funcionario = Funcionario(primeiro_nome=primeiro_nome, sobrenome=sobrenome, data_admissao=data_admissao,
                                       id_setor=setor_id, cargo_id=cargo_id)
        db.session.add(novo_funcionario)
        db.session.commit()
        return redirect(url_for('index'))  # Redireciona de volta para a página inicial após cadastrar o funcionário

    # Buscar os setores e cargos do banco de dados
    setores = Setor.query.all()
    cargos = Cargo.query.all()

    return render_template('cadastrar_funcionario.html', setores=setores, cargos=cargos)

@app.route('/cadastrar_setor', methods=['GET', 'POST'])
def cadastrar_setor():
    if request.method == 'POST':
        novo_setor = request.form['setor']
        try:
            novo_setor = Setor(setor=novo_setor)
            db.session.add(novo_setor)
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            return "Setor já existe, tente outro nome."
    return render_template('cadastrar_setor.html')

# Rota para cadastrar cargo
@app.route('/cadastrar_cargo', methods=['GET', 'POST'])
def cadastrar_cargo():
    if request.method == 'POST':
        novo_cargo = request.form['cargo']
        try:
            novo_cargo = Cargo(cargo=novo_cargo)
            db.session.add(novo_cargo)
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            return "Cargo já existe, tente outro nome."
    return render_template('cadastrar_cargo.html')

@app.route('/excluir_funcionario/<int:id>')
def excluir_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)  # Obter o funcionário pelo ID ou retornar 404 se não encontrado
    db.session.delete(funcionario)  # Excluir o funcionário do banco de dados
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar_funcionario/<int:id>', methods=['GET', 'POST'])
def editar_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    if request.method == 'POST':
        # Atualizar os detalhes do funcionário com base nos dados do formulário
        funcionario.primeiro_nome = request.form['primeiro_nome']
        funcionario.sobrenome = request.form['sobrenome']
        funcionario.id_setor = request.form['id_setor']
        funcionario.cargo_id = request.form['cargo_id']
        db.session.commit()
        return redirect(url_for('index'))
    # Buscar os setores e cargos do banco de dados
    setores = Setor.query.all()
    cargos = Cargo.query.all()
    return render_template('editar_funcionario.html', funcionario=funcionario, setores=setores, cargos=cargos)


if __name__ == '__main__':
    app.run(debug=True)
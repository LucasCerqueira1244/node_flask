import conexao from "../database/conexao.js"
import LoginRepository from "../repositores/LoginRepository.js"

class LoginController {

    async index(req, res) {
        await conexao
        const row = await LoginRepository.findAll()
        res.json(row)
    }
      
    async show(req, res) {
        await conexao
        const id = req.params.id
        const row = await LoginRepository.findByID(id)
        res.json(row)
    }

    async store(req, res) {
        try {
            await conexao
            const { username, password } = req.body; // Extrai username e password do corpo da requisição
            const user = await LoginRepository.create(username, password); // Chama o método create do repositório
    
            res.status(201).json(user); // Retorna o usuário criado com o status HTTP 201 (Created)
        } catch (error) {
            console.error('Erro ao criar usuário:', error);
            res.status(500).json({ error: 'Erro interno do servidor' }); // Retorna uma mensagem de erro genérica em caso de falha
        }
    }
        
    async update(req, res) {
        await conexao
        const usu = req.body
        const id = req.params.id
        const row = await LoginRepository.update(id, usu)
        res.json(row)
    }
    
    async delete(req, res) {
        await conexao
        const id = req.params.id
        const row = await LoginRepository.delete(id)
        res.json(row)
    }
}

export default new LoginController()
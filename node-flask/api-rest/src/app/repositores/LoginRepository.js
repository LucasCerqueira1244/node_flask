import LoginModel from '../models/loginModels.js';

class LoginRepository {
    async create(username, password) {
        try {
            const user = new LoginModel({ username, password });
            await user.save();
            return user;
        } catch (error) {
            console.error('Erro ao cadastrar usuário:', error);
            throw new Error('Não foi possível cadastrar o usuário');
        }
    }

    async findAll() {
        try {
            const users = await LoginModel.find();
            return users;
        } catch (error) {
            throw new Error('Não foi possível localizar');
        }
    }

    async findByID(id) {
        try {
            const user = await LoginModel.findById(id);
            if (!user) throw new Error('Usuário não encontrado');
            return user;
        } catch (error) {
            throw new Error('Não foi possível localizar');
        }
    }

    async update(id, usu) {
        try {
            const user = await LoginModel.findByIdAndUpdate(id, usu, { new: true });
            if (!user) throw new Error('Usuário não encontrado');
            return user;
        } catch (error) {
            throw new Error('Não foi possível atualizar');
        }
    }

    async delete(id) {
        try {
            const user = await LoginModel.findByIdAndDelete(id);
            if (!user) throw new Error('Usuário não encontrado');
            return user;
        } catch (error) {
            throw new Error('Não foi possível deletar');
        }
    }
}

export default new LoginRepository();

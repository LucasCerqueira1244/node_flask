import mongoose from "mongoose";

const conexao = mongoose.connect('mongodb://localhost:27017/login', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

conexao.then(() => {
    console.log("Conexão com MongoDB estabelecida com sucesso!");
}).catch((erro) => {
    console.error("Erro ao conectar ao MongoDB:", erro);
});

export default conexao;
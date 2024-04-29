import { Router } from "express";
import LoginController from '../src/app/controllers/LoginController.js'

const router = Router()
let errorMessage = ''

//rotas
router.get('/', (req, res) => {
    res.render('index')
})
router.post('/index', (req, res) => {
    const { username, password } = req.body;
    if (username === 'admin' && password === '1244') {
        res.render('empresa', { username });
    } else {
        errorMessage = 'Credenciais inválidas. Tente novamente.'; 
        res.redirect('/'); 
    }
}) 
router.get('/login', LoginController.index)
router.get('/login/:id', LoginController.show)
router.post('/login', LoginController.store)
router.put('/login/:id', LoginController.update)
router.delete('/login/:id', LoginController.delete)

export default router
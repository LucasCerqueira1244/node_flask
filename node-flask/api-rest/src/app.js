import express from 'express';
import routes from './routes.js';
import bodyParser from 'body-parser';
import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(routes);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

export default app;

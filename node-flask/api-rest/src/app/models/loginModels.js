import mongoose from 'mongoose';

const { Schema, model } = mongoose;

const loginSchema = new Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

const LoginModel = model('User', loginSchema);

export default LoginModel;
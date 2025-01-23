import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useApi from '../hooks/useApi';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';

function Register() {
  const {post, loading, error } = useApi("http://127.0.0.1:8000/users")
  const [email, setEmail] = useState('');
  const [nombre, setNombre] = useState('');
  const [password, setPassword] = useState('');
  const history = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // await register(email, password);
      const userData = { nombre: nombre, email, password };
      await post ('/register', userData);
      history('/login');
    } catch (error) {
      console.error('Error al registrarse:', error);
    }
  };

  return (
    <div className="container">
      <h1>Registrarse</h1>
      <form onSubmit={handleSubmit}>
      <InputField
          type="name"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          placeholder="Nombre"
          required
        />
        <InputField
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <InputField
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Contraseña"
          required
        />
        {/* <SubmitButton text="Registrarse" /> */}
        <SubmitButton text = {loading ? "Registrando..." : "Registrarse"} disabled = {loading}/>
      </form>
      {error && <p className="error">Error: {error.message}</p>}
    </div>
  );
}

export default Register;


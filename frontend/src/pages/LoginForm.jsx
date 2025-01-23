import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import '../styles/Pages.css';
import useApi from '../hooks/useApi';

const LoginForm = () =>  {
  const {post, loading, error } = useApi("http://127.0.0.1:8000/users")
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState(null);
  

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await post("/login", { email, password });
      setToken(response.token);
      alert("Inicio de sesión exitoso");
    } catch (err) {
      console.error('Error logging in:', err);
    }
  };

  return (
    <div className="container">
      <h1>Iniciar Sesión</h1>
      <form onSubmit={handleLogin} className="form">
        <InputField
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <InputField
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Contraseña"
          required
        />
        <SubmitButton text={loading ? "Cargando..." : "Iniciar Sesión"}/>
        {error && (
                <p style={{ color: "red" }}>
                    {error.response?.data?.message || "Ocurrió un error inesperado. Intenta de nuevo más tarde."}
                </p>
            )}
      </form>
    </div>
  );
}

export default LoginForm;

import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { changePassword } from '../services/api';
import "../styles/Pages.css";
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';

function ChangePassword() {
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');
  const location = useLocation();
  const history = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = new URLSearchParams(location.search).get('token');
    try {
      const response = await changePassword(token, newPassword);
      setMessage(response.data.message);
      setTimeout(() => history.push('/login'), 3000);
    } catch (error) {
      console.error('Error changing password:', error);
      setMessage('An error occurred. Please try again.');
    }
  };

  return (
    <div className="container">
      <h1>Cambiar Contraseña</h1>
      <form onSubmit={handleSubmit}>
        <InputField
          type="password"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          placeholder="Contraseña Nueva"
          required
        />
        <SubmitButton text="Cambiar Contraseña" />
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default ChangePassword;


import React, { useState } from 'react';
import { resetPassword } from '../services/api';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';

function ResetPassword() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await resetPassword(email);
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error resetting password:', error);
      setMessage('An error occurred. Please try again.');
    }
  };

  return (
    <div className='container'>
      <h1>Reiniciar Contraseña</h1>
      <form onSubmit={handleSubmit}>
        <InputField
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <button type="submit">Reiniciar Contraseña</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default ResetPassword;


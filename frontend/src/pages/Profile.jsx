import React, { useState, useEffect } from 'react';
import { requestValidatorStatus } from '../services/api';

function Profile() {
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Fetch user data here
  }, []);

  const handleRequestValidatorStatus = async () => {
    try {
      const response = await requestValidatorStatus();
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error requesting validator status:', error);
      setMessage('An error occurred. Please try again.');
    }
  };

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className='container'>
      <h1>Perfil del Usuario</h1>
      <p>Email: {user.email}</p>
      <p>Puntos: {user.points}</p>
      <p>{user.is_validator ? 'Validador' : 'Principiante'}</p>
      {!user.is_validator && user.points >= 100 && (
        <button onClick={handleRequestValidatorStatus}>Request Validator Status</button>
      )}
      {message && <p>{message}</p>}
    </div>
  );
}

export default Profile;


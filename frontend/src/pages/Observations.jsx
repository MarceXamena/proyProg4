import React, { useState } from 'react';
import { createObservation } from '../services/api';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';

function Observations() {
  const [observation, setObservation] = useState({
    date_time: '',
    location: '',
    sky_conditions: '',
    equipment: '',
    description: '',
    celestial_object_id: '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createObservation(observation);
      alert('Observación Agregada');
      // Reset form or redirect
    } catch (error) {
      console.error('Error al enviar Observación:', error);
    }
  };

  const handleChange = (e) => {
    setObservation({ ...observation, [e.target.name]: e.target.value });
  };

  return (
    <div className="container">
      <h1>Enviar una Observación</h1>
      <form onSubmit={handleSubmit}>
        <InputField
          type="datetime-local"
          name="date_time"
          value={observation.date_time}
          onChange={handleChange}
          required
        />
        <InputField
          type="text"
          name="location"
          value={observation.location}
          onChange={handleChange}
          placeholder="Ubicación"
          required
        />
        <InputField
          type="text"
          name="sky_conditions"
          value={observation.sky_conditions}
          onChange={handleChange}
          placeholder="Condiciones del Cielo"
          required
        />
        <InputField
          type="text"
          name="equipment"
          value={observation.equipment}
          onChange={handleChange}
          placeholder="Equipo Utilizado"
          required
        />
        <textarea
          name="description"
          value={observation.description}
          onChange={handleChange}
          placeholder="Descripción"
          required
        />
        <InputField
          type="number"
          name="celestial_object_id"
          value={observation.celestial_object_id}
          onChange={handleChange}
          placeholder="ID del Objeto"
          required
        />
        <SubmitButton text="Enviar Observación" />
      </form>
    </div>
  );
}

export default Observations;


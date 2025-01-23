import React, { useState, useEffect } from 'react';
import '../styles/Pages.css';
import { getCelestialObjects } from '../services/api';

function CelestialObjects() {
  const [celestialObjects, setCelestialObjects] = useState([]);

  useEffect(() => {
    const fetchCelestialObjects = async () => {
      try {
        const response = await getCelestialObjects();
        setCelestialObjects(response.data);
      } catch (error) {
        console.error('Error fetching celestial objects:', error);
      }
    };

    fetchCelestialObjects();
  }, []);

  return (
    <div className="container">
      <h1>Objetos Celestes</h1>
      <ul>
        {celestialObjects.map((object) => (
          <li key={object.id}>
            {object.name} - {object.object_type}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CelestialObjects;

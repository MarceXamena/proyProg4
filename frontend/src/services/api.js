import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});

export const login = (email, password) => 
  api.post('/token', { username: email, password }, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } });

export const register = (email, password) => 
  api.post('/users/', { email, password });

export const resetPassword = (email) => 
  api.post('/reset-password/', { email });

export const changePassword = (token, new_password) => 
  api.post('/change-password/', { token, new_password });

export const requestValidatorStatus = () => 
  api.post('/request-validator-status/');

export const getCelestialObjects = (skip = 0, limit = 100) => 
  api.get(`/celestial_objects/?skip=${skip}&limit=${limit}`);

export const createObservation = (observationData) => 
  api.post('/observations/', observationData);

export default api;


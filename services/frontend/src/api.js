// Base URL of the Flask backend; set VITE_API_URL at build time to change it
export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5001'

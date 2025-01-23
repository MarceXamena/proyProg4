import { useState, useEffect } from "react";
import axios from "axios";

const useApi = (baseUrl) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Función genérica para realizar peticiones
    const fetchData = async (endpoint, method = "GET", body = null, config = {}) => {
        setLoading(true);
        setError(null);

        try {
            const response = await axios({
                url: `${baseUrl}${endpoint}`,
                method,
                data: body,
                ...config,
            });
            setData(response.data);
            return response.data; // Devuelve la respuesta para un uso directo
        } catch (err) {
            setError(err);
            console.error("API error:", err);
            throw err; // Lanza el error para manejarlo en componentes
        } finally {
            setLoading(false);
        }
    };

    // Funciones específicas para cada método HTTP
    const get = (endpoint, config = {}) => fetchData(endpoint, "GET", null, config);
    const post = (endpoint, body, config = {}) => fetchData(endpoint, "POST", body, config);
    const put = (endpoint, body, config = {}) => fetchData(endpoint, "PUT", body, config);
    const del = (endpoint, config = {}) => fetchData(endpoint, "DELETE", null, config);

    return { data, loading, error, get, post, put, del };
};

export default useApi;

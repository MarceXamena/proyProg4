import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import Router from "./routes/Router"; // Asegúrate de que este import sea correcto

const App = () => {
    return <RouterProvider router={Router} />
    
};

export default App; // Exportación por defecto

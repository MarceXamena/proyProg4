import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import "../styles/Navbar.css";
import Logo from "../assets/Logo.jpg";

function Navbar() {
    const { state, actions } = useAuth();
    if (!state || typeof state.isAuthenticated === 'undefined') {
      return <div>Loading...</div>
    }

    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">
                    <img src={Logo} alt="Astros Logo" className="logo-image" />
                </Link>
            </div>
            <ul className="navbar-list">
                <li className="navbar-item">
                    <Link to="/" className="navbar-link">Inicio</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/celestial-objects" className="navbar-link">Objetos Celestes</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/observations" className="navbar-link">Observaciones</Link>
                </li>
                {state.isAuthenticated ? (
          <>
            <li className="navbar-item"><Link to="/profile" className="navbar-link">Perfil</Link></li>
            <li className="navbar-item">
              <button onClick={actions.logout} className="navbar-link">Cerrar Sesión</button>
            </li>
          </>
        ) : (
          <>
            <li className="navbar-item"><Link to="/login" className="navbar-link">Iniciar Sesión</Link></li>
            <li className="navbar-item"><Link to="/register" className="navbar-link">Registrarse</Link></li>
          </>
        )}
            </ul>
        </nav>
    );
}

export default Navbar;

import { createContext, useReducer, useContext } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const AuthContext = createContext({
    state: {},
    actions: {},
});

const ACTIONS = {
    LOGIN: "LOGIN",
    LOGOUT: "LOGOUT",
};

function reducer(state, action) {
    switch (action.type) {
        case ACTIONS.LOGIN:
            return {
                ...state,
                user__id: action.payload.id,
                name: action.payload.nombre,
                email: action.payload.email,
                nivel_id: action.payload.nivel_id,
                puntos: action.payload.puntos,
                token: action.payload.token,
                isAuthenticated: true,
            };
        case ACTIONS.LOGOUT:
            return {
                isAuthenticated: false,
            };
        default:
            return state;
    }
}

function AuthProvider({ children }) {
    const [state, dispatch] = useReducer(reducer, {
        name: localStorage.getItem("name") || "",
        user__id: localStorage.getItem("id") || null,
        email: localStorage.getItem("email") || "",
        nivel_id: localStorage.getItem("nivel_id") || 0,
        puntos: localStorage.getItem("puntos") || 0,
        token: localStorage.getItem("authToken") || "",
        isAuthenticated: localStorage.getItem("authToken") ? true : false,
    });
    const navigate = useNavigate();
    const location = useLocation();

    const actions = {
        login: (token, user__id, nombre, email, nivel_id, puntos) => {
            dispatch({
                type: ACTIONS.LOGIN,
                payload: { token, user__id, nombre, email, nivel_id, puntos },
            });
            
            localStorage.setItem("authToken", token);
            localStorage.setItem("name", nombre);
            localStorage.setItem("id", user__id);
            localStorage.setItem("email", email);
            localStorage.setItem("nivel_id", nivel_id);
            localStorage.setItem("puntos", puntos);
            
            const origin = location.state?.from?.pathname || "/";
            navigate(origin);
        },
        logout: () => {
            dispatch({ type: ACTIONS.LOGOUT });
            localStorage.removeItem("authToken");
            localStorage.removeItem("user__id");
            localStorage.removeItem("name");
            localStorage.removeItem("email");
            localStorage.removeItem("nivel_id");
            localStorage.removeItem("puntos");
        },
    };

    return (
        <AuthContext.Provider value={{ state, actions }}>
            {children}
        </AuthContext.Provider>
    );
}

function useAuth(type = "state") {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error("useAuth must be used within an AuthProvider");
    }
    return context[type];
}

export { AuthContext, AuthProvider, useAuth };
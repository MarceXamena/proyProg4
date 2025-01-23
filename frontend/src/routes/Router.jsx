import { createBrowserRouter } from "react-router-dom";
import ResetPassword from "../pages/ResetPassword";
import Register from "../pages/Register";
import Profile from "../pages/Profile";
import Observations from "../pages/Observations";
import LoginForm from "../pages/LoginForm";
import Home from "../pages/Home";
import ChangePassword from "../pages/ChangePassword";
import CelestialObjects from "../pages/CelestialObjects";
import Layout from "./Layout";
import NotFound from "../pages/NotFound";

const Router = createBrowserRouter([
    {
        element: <Layout />,
        children: [
            {
                // index: true,
                path: "/",
                element: <Home />,
                errorElement: <NotFound />,
            },
            {
                path: "celestial-objects",
                element: <CelestialObjects />,
                errorElement: <NotFound />,
            },
            {
                path: "observations",
                element: <Observations />,
                errorElement: <NotFound />,
            },
            {
                path: "profile",
                element: <Profile />,
                errorElement: <NotFound />,
            },
            {
                path: "register",
                element: <Register />,
                errorElement: <NotFound />,
            },
            {
                path: "reset-password",
                element: <ResetPassword />,
                errorElement: <NotFound />,
            },
            {
                path: "change-password",
                element: <ChangePassword />,
                errorElement: <NotFound />,
            },
            {
                path: "/login",
                element: <LoginForm />,
                errorElement: <NotFound />,
            },
            {
                path: "*",
                element: <NotFound />            
            }
        ]
    }
]);

export default Router;
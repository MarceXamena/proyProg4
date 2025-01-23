import { Outlet, useLocation } from "react-router-dom";
import { AuthProvider } from "../contexts/AuthContext";
import Navbar from "../components/Navbar";
// import Footer from "../components/Footer/Footer";
export default function Layout() {
    const { pathname } = useLocation();
    // const shouldRenderNavbar = !["/login"].includes(pathname);
    return (
        <AuthProvider>
            {/* {shouldRenderNavbar && <Navbar />} */}
            <Navbar />
            <Outlet />
        </AuthProvider>
    );
}

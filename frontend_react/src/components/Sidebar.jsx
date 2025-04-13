// components/Sidebar.jsx
import React from "react";
import { NavLink } from "react-router-dom";

const Sidebar = () => {
    return (
        <nav className="sidebar">
            <ul>
                <li><NavLink to="/login"    className="nav-link"><i className="fas fa-sign-in-alt"></i> Login</NavLink></li>
                <li><NavLink to="/register" className="nav-link"><i className="fas fa-user-plus">  </i> Register</NavLink></li>
                <li><NavLink to="/invoice"   className="nav-link"><i className="fas fa-upload">  </i> Invoice</NavLink></li>
            </ul>
        </nav>
    );
};

export default Sidebar;

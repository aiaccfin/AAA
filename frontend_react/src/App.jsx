// App.jsx
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./apps/Login";
import Invoices from "./apps/Invoices";
import Register from "./apps/Register";
import Sidebar from "./components/Sidebar"; // Import Sidebar
import "./css/App.scss"; // Import SCSS for styling

function App() {
    return (
        <Router>
            <div className="app-container">
                <Sidebar /> {/* Sidebar stays fixed */}
                <div className="main-content">
                    <Routes>
                        <Route path="/" element={<Login />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        <Route path="/invoice" element={<Invoices />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;

// src/components/Dashboard.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
    const navigate = useNavigate();
    const username = localStorage.getItem('username');
    console.log(username)

    const handleLogout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('username');
        navigate('/login');
    };

    return (
        <div>
            <h2>Hi, {username}!</h2>
            <button onClick={() => navigate('/profile')}>Profile</button>
            <button onClick={() => navigate('/change-password')}>Change Password</button>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Dashboard;

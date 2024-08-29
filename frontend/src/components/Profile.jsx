// src/components/Profile.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Profile = () => {
    const [userData, setUserData] = useState({});
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get('http://127.0.0.1:8000/api/users/profile/', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                });
                setUserData(response.data);
            } catch (error) {
                console.error('Error fetching profile data', error);
            }
        };
        fetchProfile();
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('username');
        navigate('/login');
    };

    return (
        <div>
            <h2>Profile</h2>
            <p><strong>Username:</strong> {userData.username}</p>
            <p><strong>Email:</strong> {userData.email}</p>
            <p><strong>Date Joined:</strong> {new Date(userData.date_joined).toLocaleDateString()}</p>
            <p><strong>Last Updated:</strong> {new Date(userData.last_login).toLocaleDateString()}</p>
            <button onClick={() => navigate('/')}>Back to Dashboard</button>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Profile;

import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ element: Element }) => {
    const token = localStorage.getItem('access_token');

    return token ? <Element /> : <Navigate to="/login" />;
};

export default ProtectedRoute;

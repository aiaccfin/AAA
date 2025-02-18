import React, { useState, useContext } from 'react';
import userContext from '../context/UserContext';
import { Link } from 'react-router-dom';

import {MDBContainer,MDBInput,MDBCheckbox,MDBBtn,} from 'mdb-react-ui-kit';

import { decodeToken } from '../utils/auth';


function LoginMG() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null); // State for success message

    const { setUser } = useContext(userContext);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:8080/user/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            localStorage.setItem("token", data.access_token); // Store token
            // await fetchUserInfo();
            const token = localStorage.getItem("token");
            setUser(data);  // Update React state
            
            const decodedData = decodeToken(token);
            setSuccessMessage(`User Token Info:<br>${JSON.stringify(decodedData, null, 2)}`);

        } catch (error) {
            console.error('Error making request:', error);
            setError('You not authorized to use the system. Call admin for help.');
            setSuccessMessage(null); // Clear success message
        }
    };

    const fetchUserInfo = async () => {
        const token = localStorage.getItem("token");
        console.log('retreive from local:')
        console.log(token)
        if (!token) return;
    
        try {
            const response = await fetch("http://localhost:8080/user/me", {
                headers: { Authorization: `Bearer ${token}` },
            });

            console.log("Response Status:", response.status);
            const responseData = await response.json();
            console.log("Response Data:", responseData);
    
            if (response.status === 401) {  // ✅ Handle Unauthorized case
                console.warn("Invalid token, logging out...");
                localStorage.removeItem("token");
                return;
            }
            
            if (!response.ok) throw new Error("Failed to fetch user info");
    
            setUser(responseData);  // Update React state
            const userInfoHtml = Object.entries(responseData)
                .map(([key, value]) => `<strong>${key}:</strong> ${value}`)
                .join("<br>");
            setSuccessMessage(`User Info:<br>${userInfoHtml}`);

        } catch (error) {
            console.error("User info error:", error);
        }
    };
    
    return (
        <MDBContainer className="p-3 my-5 d-flex flex-column w-50">
            <form onSubmit={handleSubmit}>
                <MDBInput
                    wrapperClass='mb-4'
                    label='MG Name'
                    id='form1'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <MDBInput
                    wrapperClass='mb-4'
                    label='MG Pwd'
                    id='form2'
                    type='password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <div className="d-flex justify-content-between mx-3 mb-4">
                    <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Remember me' />
                    <a href="#!">Forgot password?</a>
                </div>

                {error && <div style={{ color: 'red' }}>{error}</div>}
                {/* {successMessage && <div style={{ color: 'green' }}>{successMessage}</div>} Display success message */}
                {successMessage && (
                    <div
                        style={{ color: 'green' }}
                        dangerouslySetInnerHTML={{ __html: successMessage }}
                    />
                )} {/* Display success message with HTML content */}

                <MDBBtn type="submit" className="mb-4">Sign in</MDBBtn>
            </form>

            <div className="text-center">
                <p>Not a member? <Link to="/register">Register</Link></p>
            </div>
        </MDBContainer>
    );
}

export default LoginMG;

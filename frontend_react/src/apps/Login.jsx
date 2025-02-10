import React, { useState, useContext } from 'react';
import userContext from '../context/UserContext';
import { Link } from 'react-router-dom';

import {MDBContainer,MDBInput,MDBCheckbox,MDBBtn,} from 'mdb-react-ui-kit';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null); // State for success message

    const { setUser } = useContext(userContext);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('https://492ogn6a27.execute-api.us-east-2.amazonaws.com/l1/login', {
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

            if (data.success) {
                const { firstname, lastname, company, email } = data.user;
                setUser(data.user);
                setSuccessMessage(
                    `Welcome, <strong>${firstname} ${lastname}</strong>! ` +
                    `You are logged in as: ${username}.<br>` +
                    `Company: ${company}<br>` +
                    `Email: ${email}`
                );
                setError(null); // Clear any previous errors
            } else {
                setError('Invalid login credentials');
                setSuccessMessage(null); // Clear success message
            }
        } catch (error) {
            console.error('Error making request:', error);
            setError('You are not authorized to use the system. Call admin for help.');
            setSuccessMessage(null); // Clear success message
        }
    };

    return (
        <MDBContainer className="p-3 my-5 d-flex flex-column w-50">
            <form onSubmit={handleSubmit}>
                <MDBInput
                    wrapperClass='mb-4'
                    label='User Name'
                    id='form1'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <MDBInput
                    wrapperClass='mb-4'
                    label='Password'
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

export default Login;

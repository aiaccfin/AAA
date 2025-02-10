// main.jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import UserContextProvider from './context/UserContextProvider'; // Import the UserContextProvider
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <UserContextProvider>
            <App />
        </UserContextProvider>
    </StrictMode>,
);

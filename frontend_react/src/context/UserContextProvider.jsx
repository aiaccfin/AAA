// UserContextProvider.jsx

import React from 'react'
import UserContext from './UserContext'

const UserContextProvider = ({ children }) => {
    // this is used to store the data 
    const [user, setUser] = React.useState(null);
    return (
        <UserContext.Provider value={{ user, setUser }}>
            {
                children
            }
        </UserContext.Provider>
    )
}

export default UserContextProvider
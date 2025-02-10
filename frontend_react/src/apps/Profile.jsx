import React, { useContext } from 'react'
import userContext from '../context/UserContext'

const Profile = () => {
  const {user,setUser} = useContext(userContext)
  const handleLogout = ()=>{
    localStorage.clear();
    setUser('');
  }


    if(!user) return <h1> plz sign in </h1>;
  return (
    <div>
      Welcome {user.username }
      your number {user.number}
    <button onClick={handleLogout}> Logout </button>
    </div>
  )
}

export default Profile
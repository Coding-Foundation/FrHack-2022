import React from 'react';
import './App.css';
import MainMap from "./components/Map";
import NavBar from "./components/NavBar";

function App() {
  return (
    <div className={"flex flex-col h-screen"}>
      <NavBar/>
      <div className={"grow"}>
      <MainMap/>
      </div>
    </div>
  );
}

export default App;

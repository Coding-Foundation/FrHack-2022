import React, {useState} from 'react';
import './App.css';
import MainMap from "./components/Map";
import NavBar from "./components/NavBar";
import SideAlert from "./components/SideAlert";
import {Antenna} from "./types/Antenna";
import {Captor} from "./types/Captor";

function App() {
  const [selectedObject, setSelectedObject]  = useState<Antenna | Captor | null>(null);

  return (
    <div className={"flex flex-col h-screen"}>
      <NavBar/>
      <div className={"flex grow"}>
        <MainMap selectObject={setSelectedObject}/>
        <SideAlert data={selectedObject}/>
      </div>
    </div>
  );
}

export default App;

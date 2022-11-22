import React, {useState} from 'react';
import './App.css';
import MainMap from "./components/Map";
import NavBar from "./components/NavBar";
import SideAlert from "./components/SideAlert";
import {Antenna} from "./types/Antenna";
import {Captor} from "./types/Captor";

function App() {
    const [selectedAntenna, setSelectedAntenna] = useState<Antenna | null>(null);
    const [selectedCaptor, setSelectedCaptor] = useState<Captor | null>(null);

    const selectObject = (antenna: Antenna | null, captor: Captor | null) => {
        setSelectedAntenna(antenna);
        setSelectedCaptor(captor);
    }

    return (
        <div className={"flex flex-col min-h-screen w-full md:h-screen md:max-h-screen"}>
            <NavBar/>
            <div className={"flex flex-col h-full w-full md:flex-row md:max-h-full"}>
                <MainMap selectObject={selectObject}/>
                <SideAlert antenna={selectedAntenna} captor={selectedCaptor}/>
            </div>
        </div>
    );
}

export default App;

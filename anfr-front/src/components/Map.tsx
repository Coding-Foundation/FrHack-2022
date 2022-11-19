import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'

const MainMap = () => {

    const position = {
        lng: 2.213749,
        lat: 46.227638
    }

    return (
        <MapContainer center={position} zoom={6} className={"map-container"}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={position}>
                <Popup>
                    A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
            </Marker>
        </MapContainer>
    );
}

export default MainMap;

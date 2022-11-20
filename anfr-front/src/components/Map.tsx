import React from "react";
import {MapContainer, TileLayer, Marker, Popup} from 'react-leaflet'
import {Icon, IconOptions} from "leaflet";
import UseCaptors from "../hooks/UseCaptors";
import UseAntennas from "../hooks/UseAntennas";
import {Antenna} from "../types/Antenna";
import AntennaIcon from "../images/antenna.png"
import {Captor} from "../types/Captor";
import cluster0Image from "../images/cluster0.png"
import cluster1Image from "../images/cluster1.png"
import cluster2Image from "../images/cluster2.png"

type Props = {
  selectObject: (antenna: Antenna | null, captor: Captor | null) => void;
}

const MainMap: React.FC<Props> = (props) => {
  const {captors} = UseCaptors();
  const {antennas} = UseAntennas();
  const clustersImages = [cluster0Image, cluster1Image, cluster2Image];
  const position = {
    lng: 2.213749,
    lat: 46.227638
  }

  const antennaIcon: Icon = new Icon<IconOptions>({
    iconUrl: AntennaIcon,
    iconSize: [50, 50]
  })

  return (
    <MapContainer center={position} zoom={6} className={"map-container"}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={position}>
        <Popup>
          A pretty CSS3 popup. <br/> Easily customizable.
        </Popup>
      </Marker>

      {
        antennas.map((antenna) => {
          return (
            <Marker eventHandlers={{
              click: () => {
                props.selectObject(antenna, null)
              }
            }} position={{lng: antenna.longitude, lat: antenna.latitude}}
                    icon={antennaIcon}
            >

            </Marker>
          )
        })
      }

      {
        captors.map((captor) => {
          const captorIcon: Icon = new Icon<IconOptions>({
            iconUrl: clustersImages[captor.cluster],
            iconSize: [50, 50]
          })
          return (
            <Marker eventHandlers={{
              click: () => {
                props.selectObject(null, captor)
              }
            }} position={{lng: captor.longitude, lat: captor.latitude}}
                    icon={captorIcon}
            >

            </Marker>
          )
        })
      }

    </MapContainer>
  );
}

export default MainMap;

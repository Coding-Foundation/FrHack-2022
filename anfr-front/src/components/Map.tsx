// @ts-nocheck
import React from "react";
import {MapContainer, TileLayer, Marker, Polygon} from 'react-leaflet'
import {Icon, IconOptions} from "leaflet";
import UseCaptors from "../hooks/UseCaptors";
import UseAntennas from "../hooks/UseAntennas";
import {Antenna} from "../types/Antenna";
import AntennaIcon from "../images/antenna.png"
import {Captor} from "../types/Captor";
import cluster0Image from "../images/cluster0.png"
import cluster1Image from "../images/cluster1.png"
import cluster2Image from "../images/cluster2.png"
import MarkerClusterGroup from "react-leaflet-markercluster";

type Props = {
  selectObject: (antenna: Antenna | null, captor: Captor | null) => void;
}

const MainMap: React.FC<Props> = (props) => {
  const {captors} = UseCaptors();
  const {antennas, supportCoords} = UseAntennas();
  const clustersImages = [cluster0Image, cluster1Image, cluster2Image];
  const position = {
    lng: 2.213749,
    lat: 46.227638
  }

  const rangeCoords = (coords: [lat: number, lng: number],azimuth: number, alpha: number) => {
    const rTerre = 6371000

      const x = Math.sin((azimuth + alpha) * Math.PI/180) * 200;
      const y = Math.cos((azimuth + alpha) * Math.PI/180) * 200;

      const deltaLatitude = y/rTerre * 180/Math.PI;
      const deltaLongitude = x/rTerre * 180/Math.PI;

      return [deltaLatitude + coords[0], deltaLongitude + coords[1]]
  }


  const antennaIcon: Icon = new Icon<IconOptions>({
    iconUrl: AntennaIcon,
    iconSize: [50, 50]
  })

    return (
    <MapContainer center={position} zoom={6} className={"w-full h-screen md:h-full"}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {
        supportCoords.map((support) => {
          return (
              <Marker
               position={{lng: support.lng, lat: support.lat}}
                      icon={antennaIcon}
              />
          )
        })
      }


      {
        antennas.map((antenna) => {
          const polyCoords = []

          polyCoords.push([antenna.latitude, antenna.longitude]);

          polyCoords.push(rangeCoords([antenna.latitude, antenna.longitude], antenna.azimut, 60));
          polyCoords.push(rangeCoords([antenna.latitude, antenna.longitude], antenna.azimut, -60));


          return (
              <>
                <Polygon positions={polyCoords} eventHandlers={{
                  click: () => {
                    props.selectObject(antenna, null)
                  }
                }} position={{lng: antenna.longitude, lat: antenna.latitude}}/>
              </>)
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
            />
          )
        })
      }
    </MapContainer>
  );
}

export default MainMap;

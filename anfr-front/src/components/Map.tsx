import React from "react";
import {MapContainer, TileLayer, Marker, Popup} from 'react-leaflet'
import {Icon, IconOptions} from "leaflet";
import UseCaptors from "../hooks/UseCaptors";
import UseAntennas from "../hooks/UseAntennas";
import {Antenna} from "../types/Antenna";
import AntennaIcon from "../images/antenna.png"
import {Captor} from "../types/Captor";

type Props = {
  selectObject: (object: Antenna | Captor) => void;
}

const MainMap: React.FC<Props> = (props) => {
  const {captors} = UseCaptors();
  const {antennas} = UseAntennas();
  const antenna: Antenna = {
    id: 1,
    position: {
      id: 1,
      azimut: 0,
      altitude: 10,
      code_insee: "100",
      code_region: "13",
      lib_dpt: "Loire atlantique",
      lib_maj_reg: "PACA",
      latitude: 47.267638,
      longitude: 3.215749
    }
  }
  const position = {
    lng: 2.213749,
    lat: 46.227638
  }

  const colors = ["000000", "FF0000", "00FF00", "0000FF", "FFFF00", "00FFFF", "FF00FF", "FFFFFF"]
  const antennaIconUrl = `https://thenounproject.com/api/private/icons/1121998/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23${colors[4]}&foregroundOpacity=1&imageFormat=png&rotation=0&token=gAAAAABjeUbo56t4uSnKDI7aF8lgYKmVDjoGoqONKiWOpPKoLh9Wx9KwXX9ME84ooh1aU3MVhZ3GIXBOpA23U18L-dN3gbGQ1Q%3D%3D`
  const antennaIcon: Icon = new Icon<IconOptions>({
    iconUrl: AntennaIcon,
    iconSize: [50, 50]
  })

  const captorIconUrl = `https://img.icons8.com/ios-glyphs/90/${colors[5]}/electrical-sensor.png`;
  const captorIcon: Icon = new Icon<IconOptions>({
    iconUrl: antennaIconUrl,
    iconSize: [50, 50]
  })

  return (
    <MapContainer center={position} zoom={6} className={"map-container"}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={position} >
        <Popup>
          A pretty CSS3 popup. <br/> Easily customizable.
        </Popup>
      </Marker>

      {
        antennas.map((antenna) => {
          return (
            <Marker eventHandlers={{
              click: () => {
                props.selectObject(antenna)
              }
            }} position={{lng: antenna.position.longitude, lat: antenna.position.latitude}}
            icon={antennaIcon}
            >

            </Marker>
          )
        })
      }

      {
        captors.map((captor) => {
          return (
            <Marker eventHandlers={{
              click: () => {
                props.selectObject(captor)
              }
            }} position={{lng: captor.longitude, lat: captor.latitude}}
                    icon={captorIcon}
            >

            </Marker>
          )
        })
      }

      <Marker icon={antennaIcon} position={{lng: antenna.position.longitude, lat: antenna.position.latitude}}>
        <div>
          test
        </div>

      </Marker>
    </MapContainer>
  );
}

export default MainMap;

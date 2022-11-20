import {Antenna} from "../types/Antenna";
import {Captor} from "../types/Captor";
import React, {useState} from "react";
import {API_URL} from "../conf.api";

type Props = {
  antenna: Antenna | null
  captor: Captor | null;
}

const SideAlert: React.FC<Props> = (props) => {
  const [firstTabSelected, setFirstTabSelected] = useState(true);

  if (!props.antenna && !props.captor)
    return <></>

  if (props.antenna) {
    const antenna = props.antenna;

    return (
      <div className="artboard artboard-horizontal phone-3">
        <div>
          {antenna.azimut}
          {antenna.altitude}
        </div>
      </div>
    )
  }
  if (!props.captor)
    return <></>

  const captor = props.captor;
  const rawResultClass = firstTabSelected ? "tab-active" : "";
  const variationResultClass = firstTabSelected ? "" : "tab-active";

  return (
    <div className="artboard artboard-horizontal phone-3 ml-8">
      <div><span>Nom du capteur:</span> <span>{captor.name}</span></div>
      <div><span>Cluster: </span> <span>{captor.cluster}</span></div>
      <div><span>Latitude: </span> <span>{captor.latitude}</span></div>
      <div><span>Longitude: </span> <span>{captor.longitude}</span></div>
      <div><span>Date de mise en service: </span> <span>{captor.creation_date}</span></div>

      <div className="tabs">
        <a className={"tab tab-lifted " + rawResultClass} onClick={() => {setFirstTabSelected(true)}}>Résultats</a>
        <a className={"tab tab-lifted " + variationResultClass} onClick={() => {setFirstTabSelected(false)}}>Variations des résultats</a>
      </div>
      <div>
        {
          firstTabSelected ? (
            <>
              <img src={`${API_URL}/raw-results/${captor.name}`} alt="captorRes"/>
              <img src={`${API_URL}/results-cluster/${captor.cluster}`} alt=""/>
            </>
          ) : (
            <>
              <img src={`${API_URL}/results/${captor.name}`} alt="captorRes"/>
              <img src={`${API_URL}/results-cluster/${captor.cluster}`} alt=""/>
            </>
          )
        }
      </div>
    </div>
  )
}

export default SideAlert;

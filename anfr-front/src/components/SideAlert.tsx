import {Antenna} from "../types/Antenna";
import {Captor} from "../types/Captor";
import React, {useState} from "react";
import {API_URL} from "../conf.api";
import UseTransmitters from "../hooks/UseTransmitters";

type Props = {
    antenna: Antenna | null
    captor: Captor | null;
}

const SideAlert: React.FC<Props> = (props) => {
    const [firstTabSelected, setFirstTabSelected] = useState(true);
    const id = props.antenna?.id || 0;
    const {transmitters} = UseTransmitters(id);
    if (!props.antenna && !props.captor)
        return <></>

    if (props.antenna) {
        const antenna = props.antenna;


        return (
            <div className="artboard artboard-horizontal phone-3 mx-8">
              <h2 className={"font-bold"}>Information sur l'antenne :</h2>
                <div className={"mt-8"}><span className={"font-semibold"}>Id de l'antenne: </span> <span>{antenna.id}</span></div>
                <div className={"mt-2"}><span className={"font-semibold"}>Altitude: </span> <span>{antenna.altitude}</span></div>
                <div className={"mt-2"}><span className={"font-semibold"}>Azimut: </span> <span>{antenna.azimut}</span></div>
                <div className={"mt-2"}><span className={"font-semibold"}>Longitude: </span> <span>{antenna.longitude}</span></div>
                <div className={"mt-2"}><span className={"font-semibold"}>Latitude: </span> <span>{antenna.latitude}</span></div>

              <h2 className={"font-bold mt-8"}>Information sur les émetteurs :</h2>
              <div className={"mt-2 overflow-y-scroll max-h-60"}>
                {
                    transmitters && transmitters.map((transmitter) => (
                      <div className={"mt-4"}>
                        <div><span className={"font-semibold mt-2"}>Id de l'émeteur: </span> <span>{transmitter.id}</span></div>
                        <div><span className={"font-semibold mt-2"}>Nom: </span> <span>{transmitter.name}</span></div>
                        <div><span className={"font-semibold mt-2"}>Date de création: </span> <span>{transmitter.creation_date}</span></div>
                        <div><span className={"font-semibold mt-2"}>Génération: </span> <span>{transmitter.generation}</span></div>
                        <div><span className={"font-semibold mt-2"}>Opérateur: </span> <span>{transmitter.operator}</span></div>
                      </div>
                    ))
                  }
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
        <div className="artboard artboard-horizontal phone-3 mx-8">
            <div className={"mt-8"}><span className={"font-semibold"}>Nom du capteur:</span> <span>{captor.name}</span></div>
            <div className={"mt-2"}><span className={"font-semibold"}>Cluster: </span> <span>{captor.cluster}</span></div>
            <div className={"mt-2"}><span className={"font-semibold"}>Latitude: </span> <span>{captor.latitude}</span></div>
            <div className={"mt-2"}><span className={"font-semibold"}>Longitude: </span> <span>{captor.longitude}</span></div>
            <div className={"mt-2"}><span className={"font-semibold"}>Date de mise en service: </span> <span>{captor.creation_date}</span></div>

            <div className="tabs my-4">
                <a className={"tab tab-lifted " + rawResultClass} onClick={() => {
                    setFirstTabSelected(true)
                }}>Résultats</a>
                <a className={"tab tab-lifted " + variationResultClass} onClick={() => {
                    setFirstTabSelected(false)
                }}>Variations des résultats</a>
            </div>
            <div>
                {
                    firstTabSelected ? (
                        <>
                            <span>Moyenne des résultats sur une semaine</span>
                            <img src={`${API_URL}/raw-results/${captor.name}`} alt="captorRes"/>
                        </>
                    ) : (
                        <>
                            <div>

                                <span>Moyenne de la variation des résultats sur une semaine du capteur</span>
                                <img src={`${API_URL}/results/${captor.name}`} alt="captorRes"/>
                            </div>
                            <div className={"mt-4"}>
                                <span>Moyenne de la variation des résultats sur une semaine du comportement type</span>
                                <img src={`${API_URL}/results-cluster/${captor.cluster}`} alt=""/>
                            </div>
                        </>
                    )
                }
            </div>
        </div>
    )
}

export default SideAlert;

import {useEffect, useState} from "react";
import {Transmitter} from "../types/Transmitter";
import axios from "axios";

const UseTransmitters = (antennaId: number) => {
    const [transmitters, setTransmitters] = useState<Transmitter[]>([]);


    const fetchTransmitters = async () => {
        try {
            const {data} = await axios.get<Transmitter[]>("transmitters/" + antennaId);
            setTransmitters(data);
        } catch (e) {
            console.log(e);
        }
    }


    useEffect(() => {
        fetchTransmitters()
    }, [])

    return {transmitters}
}

export default UseTransmitters;

import {useEffect, useState} from "react";
import {Transmitter} from "../types/Transmitter";
import axios from "axios";

const UseTransmitters = (antennaId: number) => {
    const [transmitters, setTransmitters] = useState<Transmitter[]>([]);


    const fetchTransmitters = async () => {
        try {
            let {data} = await axios.get<Transmitter[]>("transmitters/" + antennaId);
            if (!data)
                data = []
            setTransmitters(data);
        } catch (e) {
            console.log(e);
        }
    }


    useEffect(() => {
        fetchTransmitters()
    }, [antennaId])

    return {transmitters}
}

export default UseTransmitters;

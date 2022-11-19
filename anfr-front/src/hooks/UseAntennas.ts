import {useEffect, useState} from "react";
import axios from "axios";
import {Antenna} from "../types/Antenna";

const UseAntennas = () => {
  const [antennas, setAntennas] = useState<Antenna[]>([])

  const fetchAntennas = async () => {
    try {
      const {data} = await axios.get<Antenna[]>("antennas");
      setAntennas(data);
    } catch (e) {
      console.log(e);
    }
  }

  useEffect(() => {
    fetchAntennas()
  }, [])

  return {antennas}
}

export default UseAntennas;

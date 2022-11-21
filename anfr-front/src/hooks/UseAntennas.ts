import {useEffect, useState} from "react";
import axios from "axios";
import {Antenna} from "../types/Antenna";

const UseAntennas = () => {
  const [antennas, setAntennas] = useState<Antenna[]>([])
  const [supportCoords, setSupportCoords] = useState<{lat: number, lng: number}[]>([])

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

  const computeSupportCoords = () => {
    const keys = antennas.map((antenna) => {
      return antenna.latitude + " " + antenna.longitude
    })
    // @ts-ignore
    const nonDuplicateKeys = [...new Set(keys)];

    const result = nonDuplicateKeys.map(key => {
      const coords = key.split(" ")
      return {lat: +coords[0],lng:  +coords[1]}

    })
    setSupportCoords(result)
  }

  useEffect(() => {
    computeSupportCoords()
  }, [antennas])

  return {antennas, supportCoords}
}

export default UseAntennas;

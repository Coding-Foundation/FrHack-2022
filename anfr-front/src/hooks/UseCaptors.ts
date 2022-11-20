import {useEffect, useState} from "react";
import {Captor} from "../types/Captor";
import axios from "axios";

const UseCaptors = () => {
  const [captors, setCaptors] = useState<Captor[]>([])

  const fetchCaptors = async () => {
    try {
      const {data} = await axios.get<Captor[]>("captors");
      setCaptors(data);
    } catch (e) {
      console.log(e);
    }
  }


  useEffect(() => {
    fetchCaptors()
  }, [])

  return {captors}
}

export default UseCaptors;

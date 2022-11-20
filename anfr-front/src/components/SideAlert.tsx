import {Antenna} from "../types/Antenna";
import {Captor} from "../types/Captor";
import React from "react";

type Props = {
  data: Antenna | Captor | null;
}


const SideAlert: React.FC<Props> = (props) => {
  if (!props.data)
    return <></>

  return (
    <div className="artboard artboard-horizontal phone-3">
      salut
    </div>
  )
}

export default SideAlert;

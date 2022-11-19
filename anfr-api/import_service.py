from models import *
import pandas as pd
from pathlib import Path


class ImportService:

    def __init__(self, database):
        self.db = database
        self.path_data = Path(f"./Challenge 3 Variation mesures sondes fixes")
        self.network_state_path = self.path_data / f"Etats reseaux telecoms"

        measure_df = pd.read_csv(self.path_data / f"Mesures_exposition_sondes_autonomes.csv", sep=";")
        mse_df = pd.read_csv(self.path_data / f"Dates_mise-en-service_sondes_autonomes.csv", sep=",")
        self.network_state_dict = {}
        for path in self.network_state_path.glob("*.csv"):
            date = path.name.split("_Etat reseaux.csv")[0]
            self.network_state_dict[date] = pd.read_csv(path.absolute(), sep=";")

    def idIsInArray(self, array, id):
        for element in array:
            if element.id == id:
                return True

        return False

    def systemIsInArray(self, array, system):
        for element in array:
            if element.name == system.name and element.generation == system.generation and element.operator == system.operator:
                return True

        return False

    def importAntenna(self):
        antennas = []
        for dict in self.network_state_dict:
            for row in dict:
                antenna = Antenna
                antenna.id = row[4]
                antenna.azimut = row[5]
                antenna.altitude = row[6]
                if not self.idIsInArray(antennas, antenna.id):
                    antennas.append(antenna)

        self.db.bulk_save_objects(antennas)
        self.db.commit()


    def importSystem(self):
        systems = []
        for dict in self.network_state_dict:
            for row in dict:
                system = SystemTelecom
                system.name = row[2]
                system.generation = row[3]
                system.operator = row[8]
                if not self.systemIsInArray(systems, system):
                    systems.append(system)

        self.db.bulk_save_objects(systems)
        self.db.commit()



        self.db.bulk_save_objects(systems)
        self.db.commit()


from pathlib import Path 
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from glob import glob
import itertools
from functools import lru_cache, cache
import matplotlib.pyplot as plt

class Dataset:
    def __init__(path_data, network_state_path):
        self.measure_df = pd.read_csv(path_data / f"Mesures_exposition_sondes_autonomes.csv", sep=";")
        self.mse_df = pd.read_csv(path_data / f"Dates_mise-en-service_sondes_autonomes.csv", sep=",")
        
        self.measure_df["datetime"] = [datetime.strptime(d, "%d/%m/%Y %H:%M") for d in measure_df["date"]]
        self.measure_df["weekday"] = [f.weekday() for f in measure_df["datetime"]]
        self.measure_df["month"] = [f.month for f in measure_df["datetime"]]
        self.measure_df["day"] = [f.day for f in measure_df["datetime"]]
        self.measure_df["hour"] = [f.hour for f in measure_df["datetime"]]
        
        
        self.network_state_dict = {}
        for path in network_state_path.glob("*.csv"):
            date = path.name.split("_Etat reseaux.csv")[0]
            self.network_state_dict[date] = pd.read_csv(path.absolute(), sep=";")
    @cache  
    def sonde_week(sonde:str):
        """Retourne évolution V/m au cours de la semaine, à deux heure près"""
        assert (measure_df["numero"]==sonde).sum(), f"la sonde {sonde} n'existe pas"
        xrange = tuple(range(7 * 12))
        res = []
        for x in xrange:
            datetime_ = datetime(2020, 1, 1) + x * timedelta(hours=2)
            res.append(measure_df[(measure_df["numero"]==sonde) & (measure_df["weekday"]==datetime_.weekday()) & ((measure_df["hour"]==datetime_.hour) | (measure_df["hour"]==datetime_.hour+1))]["E_volt_par_metre"].mean())
        plt.plot(xrange, res, "r+")
        plt.title(f"evolution sonde {sonde} en fonction jour de la semaine")
from pathlib import Path 
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from glob import glob
import itertools
import shelve, math
from functools import lru_cache, cache, cached_property
import matplotlib.pyplot as plt

class Dataset:
    def __init__(self, path_data, network_state_path):
        self.measure_df = pd.read_csv(path_data / f"Mesures_exposition_sondes_autonomes.csv", sep=";")
        self.mse_df = pd.read_csv(path_data / f"Dates_mise-en-service_sondes_autonomes.csv", sep=",")
        
        self.measure_df["datetime"] = [datetime.strptime(d, "%d/%m/%Y %H:%M") for d in self.measure_df["date"]]
        self.measure_df["weekday"] = [f.weekday() for f in self.measure_df["datetime"]]
        self.measure_df["month"] = [f.month for f in self.measure_df["datetime"]]
        self.measure_df["day"] = [f.day for f in self.measure_df["datetime"]]
        self.measure_df["hour"] = [f.hour for f in self.measure_df["datetime"]]
        
        
        self.network_state_dict = {}
        for path in network_state_path.glob("*.csv"):
            date = path.name.split("_Etat reseaux.csv")[0]
            self.network_state_dict[date] = pd.read_csv(path.absolute(), sep=";")
            
        self.sondes_names = ("Marseille_01","Marseille_02","Marseille_03","Nantes_01","Nantes_02","Nantes_03","Paris_8e_02","Paris_8e_01","Paris_8e_03","Bordeaux_02","Bordeaux_01","Bordeaux_03","Mérignac_02","Mérignac_01","Mulhouse_03","Mulhouse_01","Mulhouse_02","Talence_01","Bègles_01","Artigues-près-Bordeaux_01","Saint-Aubin-de-Médoc_01","Le Bouscat_01","Saint-Louis-de-Montferrand_01","Bouliac_01","Le Taillan-Médoc_01","Bassens_01","Le-Haillan_01","Villenave-d’Ornon_01","Saint-Médard-En-Jalles_01","Rennes_01","Rennes_05","Rennes_04","Rennes_02","Rennes_03","Bruges_01","Bordeaux_04","Parempuyre_01","Bordeaux_05","Ambares-et-Lagrave_01","Pessac_01","Carbon-Blanc_01","Martignas-sur-Jalle_01","Blanquefort_01","Lille_02","Lille_01","Lille_03","Floirac_01","Ambès_01","Lille_04","Lille_05","Cenon_01","Gradignan_01","Orléans_03","Orléans_01","Orléans_02","Saint-Vincent-de-Paul_01","Orleans_07","Orleans_06","Orleans_05","Orleans_04","Lormont_01","Strasbourg_04","Strasbourg_03","Strasbourg_02","Strasbourg_05","Strasbourg_01","Strasbourg_08","Eysines_01","Rennes_07","Rennes_08","Rennes_10","Rennes_06","Rennes_09","Strasbourg_06","Strasbourg_07")
        
    def sonde_week(self, sonde:str):
        """Retourne évolution V/m au cours de la semaine, à deux heure près.
        première val retournée : tableau de datetime
        deuxième val retournée : tableau de moyenne"""
        key_cache = f"sonde_{sonde}"
        assert (self.measure_df["numero"]==sonde).sum(), f"la sonde {sonde} n'existe pas"
        with shelve.open('icache') as db:
            if key_cache not in db:
                xrange = tuple(range(7 * 12))
                dt = []
                res = []
                for x in xrange:
                    datetime_ = datetime(2022, 11, 7) + x * timedelta(hours=2)
                    dt.append(datetime_)
                    mean = self.measure_df[(self.measure_df["numero"]==sonde) & (self.measure_df["weekday"]==datetime_.weekday()) & ((self.measure_df["hour"]==datetime_.hour) | (self.measure_df["hour"]==datetime_.hour+1))]["E_volt_par_metre"].mean() 
                    if math.isnan(mean):
                        length_ = ((self.measure_df["numero"]==sonde) & (self.measure_df["weekday"]==datetime_.weekday()) & ((self.measure_df["hour"]==datetime_.hour) | (self.measure_df["hour"]==datetime_.hour+1))).sum()
                        print(f"pb pour sonde {sonde}, avec datetiems {repr(datetime_)}, x: {x}, weekday : {datetime_.weekday()}, hour : {datetime_.hour}, len : {length_}")
                        #Path("./debug").write_text(repr(tuple(self.measure_df[(self.measure_df["numero"]==sonde) & (self.measure_df["weekday"]==datetime_.weekday()) & ((self.measure_df["hour"]==datetime_.hour) | (self.measure_df["hour"]==datetime_.hour+1))]["E_volt_par_metre"])))
                    res.append(mean)
                db[key_cache] = dt, res
            else:
                dt, res = db[key_cache]
        return dt, res
    

    def X_week(self):
        key_cache = "X_week"
        with shelve.open('cache_X_week') as db:
            if key_cache not in db:
                res = []
                for sonde in self.sondes_names:
                    dt, values = self.sonde_week(sonde)
                    res.append(values)
                res = np.array(res)
                db[key_cache] = res
            else:
                res = db[key_cache]
        return res
    
    def sonde_week_derive(self, sonde:str):
        key_cache = f"sonde_{sonde}"
        assert (self.measure_df["numero"]==sonde).sum(), f"la sonde {sonde} n'existe pas"
        with shelve.open('icache-derive') as db:
            if key_cache not in db:
                xrange = tuple(range(7 * 12))
                dt = []
                res = []
                for x in xrange:
                    datetime_1 = datetime(2022, 11, 7) + (x-1) * timedelta(hours=2)
                    datetime_2 = datetime(2022, 11, 7) + x * timedelta(hours=2)
                    dt.append(datetime_2)
                    vec1 = self.measure_df[(self.measure_df["numero"]==sonde) & (self.measure_df["weekday"]==datetime_1.weekday()) & ((self.measure_df["hour"]==datetime_1.hour) | (self.measure_df["hour"]==datetime_1.hour+1))]["E_volt_par_metre"]
                    
                    vec2 = [self.measure_df.loc[dataset.sonde_next_record(sonde)[i]]["E_volt_par_metre"] if i in dataset.sonde_next_record(sonde) else float("nan") for i in vec1.index]
                    
                    diff = np.array(vec2) - np.array(vec1)
                    diff_removed_nan = diff[~np.isnan(diff)]
                    mean = diff_removed_nan.mean()
                    
                    res.append(mean)
                db[key_cache] = dt, res
            else:
                dt, res = db[key_cache]
        return dt, res
    
    @cache
    def sonde_next_record(self, sonde:str) -> dict:
        """En clé l'index d'un record de la sonde, en valeur, l'index de record suivant"""
        result = {}
        for k,v in tuple(itertools.pairwise(self.measure_df[(self.measure_df["numero"]==sonde)]["datetime"].index)):
            if self.measure_df.loc[v]["datetime"] - self.measure_df.loc[k]["datetime"] < timedelta(hours=3):
                result[k] = v
        return result
    
    def X_week_labels(self):
        res = []
        for i in range(7*12):
            dt = datetime(2022, 11, 7) + i * timedelta(hours=2)
            f_week = ("L", "Ma", "Mer", "J", "V", "S", "D")
            res.append(f"{f_week[dt.weekday()]} - {dt.hour}H et {dt.hour+1}H")
        return res
    
    def X_week_derive(self):
        key_cache = "X_week"
        with shelve.open('cache_X_week_derive') as db:
            if key_cache not in db:
                res = []
                for sonde in self.sondes_names:
                    dt, values = self.sonde_week_derive(sonde)
                    res.append(values)
                res = np.array(res)
                db[key_cache] = res
            else:
                res = db[key_cache]
        return res
    
    
path_data = Path(f"./")
network_state_path = path_data / f"Etats reseaux telecoms"

dataset = Dataset(path_data, network_state_path)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:35:48 2024

@author: moritz
"""

# standard library
import json
import time

# Python package index
import dash_bootstrap_components as dbc
import pandas as pd
from pandas_datareader import wb  # worldbank

# %% Data Management
# %%% Connecting to an API

def get_country_ids():
    countries_raw = wb.get_countries()
    countries_raw["capitalCity"] = countries_raw["capitalCity"].replace({"": None})
    countries = countries_raw.dropna(subset=["capitalCity"])
    countries = countries[["name", "iso3c"]]
    countries = countries[countries["name"] != "Kosovo"]
    countries = countries.rename(columns={"name": "country"})
    
    return countries


# %%% Identifying the Indicators

with open("indicators.json", "r") as file:
    indicators = json.load(file)

#%%% Extracting the Data

def get_wb_data():
    """Retrieve specific world bank data from API."""
    
    countries = get_country_ids()
    time.sleep(.5)
    df = wb.download(
        indicator=(list(indicators)), country=countries["iso3c"],
        start=2005, end=2020)
    df = df.reset_index()
    df.year = df.year.astype(int)
    
    # Add country ISO3 ID to main df
    df = pd.merge(df, countries, on="country")
    df = df.rename(columns=indicators)
    
    return df
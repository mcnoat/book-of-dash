#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:35:48 2024

@author: moritz
"""

import dash_bootstrap_components as dbc
from pandas_datareader import wb #worldbank

#%% Data Management
#%%% Connecting to an API

countries_raw = wb.get_countries()
countries_raw["capitalCity"] = countries_raw["capitalCity"].replace({"": None})
countries = countries_raw.dropna(subset=["capitalCity"])
countries = countries[["name", "iso3c"]]
countries = countries[countries["name"] != "Kosovo"]
countries = countries.rename(columns={"name":"country"})

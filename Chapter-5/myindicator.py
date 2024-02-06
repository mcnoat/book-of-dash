#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:12:25 2024

@author: moritz
"""

import json
from pandas_datareader import wb

df = wb.get_indicators()[["id", "name"]]
indicator_names = [
    "Individuals using the Internet (% of population)",
    "Proportion of seats held by women in national parliaments (%)",
    "CO2 emissions (kt)",
]
df = df[
    df.name.isin(indicator_names)
]

indicator_dict = {}
for name in indicator_names:
    indicator_id = df.loc[df.name==name, "id"].values[0]
    indicator_dict[indicator_id] = name

with open("indicators.json", "w") as file:
    json.dump(indicator_dict, file, indent=2)

# Dissertation Python Script

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


df21 = pd.read_csv('data/2021_LoL_esports_match_data_from_OraclesElixir_20220606.csv')
df22 = pd.read_csv('data/2022_LoL_esports_match_data_from_OraclesElixir_20220606.csv')

# Data exploration
df21.info()
# Just shy of 150k rows with 123 columns
# Rows are a combination of Individual Player data and Team data


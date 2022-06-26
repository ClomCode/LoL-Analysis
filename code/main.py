# Dissertation Python Script

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

data_21 = pd.read_csv(
    'C:/Users/Calum/Desktop/Useful/University/Business Analytics/Dissertation/Datasets/2021_LoL_esports_match_data_from_OraclesElixir_20220606.csv')

# Data exploration
data_21.info()
data_21.head(20)
# Just shy of 150k rows with 123 columns
# Rows are a combination of Individual Player data and Team data


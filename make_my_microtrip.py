import pandas as pd
import random

df = pd.read_csv('vbox-data/n-k right.csv')
for i, row in df.iterrows():
    if df.loc[i, 'Speed (km/h)'] < 1:
        df.loc[i, 'Speed (km/h)'] = 0

df2 = df[['Speed (km/h)', 'Elapsed time (s)', 'Longitudinal acceleration (g)']]

min_rows_per_microtrip = 50
max_rows_per_microtrip = 200

microtrips = []

while len(df2) > max_rows_per_microtrip:
    num_rows = random.randint(min_rows_per_microtrip, max_rows_per_microtrip)
    microtrip = df2.iloc[:num_rows]
    microtrips.append(microtrip)
    df2 = df2.iloc[num_rows:]

if not df2.empty:
    microtrips.append(df2)

for i, microtrip in enumerate(microtrips):
    file_name = f'microtrips/n_k_right/microtrip_{i + 1}.csv'
    microtrip.to_csv(file_name, index=False)

# import pandas as pd

# df = pd.read_csv('n-k sunday.csv')
# df2 = df[['Speed (km/h)', 'Elapsed time (s)', 'Longitudinal acceleration (g)']]
# rows = 200

# total_trips = len(df) // rows + 1  

# for i in range(total_trips):
#     start_index = i * rows
#     end_index = start_index + rows
#     micro = df.iloc[start_index:end_index]
#     file_name = f'microtrips/n_k_sunday/microtrip_{i + 1}.csv'
#     micro.to_csv(file_name, index=False)
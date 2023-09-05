import os
import pandas as pd
import random

parent_folder = 'vbox-data'

csv_files = [f for f in os.listdir(parent_folder) if f.endswith('.csv')]

min_rows_per_microtrip = 100
max_rows_per_microtrip = 100

for csv_file in csv_files:
    df = pd.read_csv(os.path.join(parent_folder, csv_file))

    df['Speed (km/h)'] = df['Speed (km/h)'].apply(lambda x: 0 if x < 1 else x)

    df2 = df[['Speed (km/h)', 'Elapsed time (s)', 'Longitudinal acceleration (g)']]

    microtrips = []

    while len(df2) > max_rows_per_microtrip:
        num_rows = random.randint(min_rows_per_microtrip, max_rows_per_microtrip)
        microtrip = df2.iloc[:num_rows]
        microtrips.append(microtrip)
        df2 = df2.iloc[num_rows:]

    if not df2.empty:
        microtrips.append(df2)

    output_folder = csv_file.replace('-', '_').replace(' ', '_').replace('.csv', '')
    output_folder_path = os.path.join('microtrips', output_folder)
    os.makedirs(output_folder_path, exist_ok=True)

    for i, microtrip in enumerate(microtrips):
        file_name = os.path.join(output_folder_path, f'microtrip_{i + 1}.csv')
        microtrip.to_csv(file_name, index=False)

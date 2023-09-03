import os
import pandas as pd

csv_directory = 'microtrips/n_k_sunday'

results = []

for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(file_path)

        avg_speed = df['Speed (km/h)'].mean()
        total_time = df.shape[0]
        idle_time = df[df['Speed (km/h)'] == 0].shape[0]
        idle_time_percentage = (idle_time / total_time) * 100

        results.append({'microtrip': filename, 'avg speed': avg_speed, 'idle time %': idle_time_percentage})

results_df = pd.DataFrame(results)
# results_df.to_csv('results.csv', index=False)
results_df.to_csv('results.csv', index=False, mode='a', header=False)
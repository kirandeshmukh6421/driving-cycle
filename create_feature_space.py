import os
import pandas as pd

parent_directory = 'microtrips' 

results = []

for root, _, files in os.walk(parent_directory):
    for filename in files:
        if filename.endswith(".csv"):
            file_path = os.path.join(root, filename)
            df = pd.read_csv(file_path)

            avg_speed = df['Speed (km/h)'].mean()
            avg_acc = df['Longitudinal acceleration (g)'].mean()
            total_time = df.shape[0]
            idle_time = df[df['Speed (km/h)'] == 0].shape[0]
            idle_time_percentage = (idle_time / total_time) * 100

            results.append({'microtrip': filename, 'avg speed': avg_speed, 'idle time %': idle_time_percentage, 'avg long. acceleration': avg_acc})

results_df = pd.DataFrame(results)
output_csv_path = 'feature_space.csv'

if not os.path.exists(output_csv_path):
    results_df.to_csv(output_csv_path, index=False)
else:
    results_df.to_csv(output_csv_path, index=False, mode='a', header=False)

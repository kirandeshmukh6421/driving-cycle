import os
import pandas as pd

input_folder = 'vbox-data' 

csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

for input_file in csv_files:
    input_path = os.path.join(input_folder, input_file)
    df = pd.read_csv(input_path)
    filtered_df = df[df['Speed (km/h)'] <= 45]
    filtered_df.to_csv(input_path, index=False)
    print(f"Filtered data saved to {input_path}")

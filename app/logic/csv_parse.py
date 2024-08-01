import csv
from datetime import datetime
"""CLIENT CSV SHOULD LOOK LIKE THIS: 
CLIENT_NAME, SERVICES, AVAILABLE_TIMES"""
# Function to parse CSV file and create a list of candlestick objects
async def load_csv(file_path):
    trainer_list = []
    
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter='\t')
            next(csvreader)  # Skip the header row
            
            for row in csvreader:
                
                trainer = {
                    "name": # name of trainer 
                    "clients": [] #{"name": NAME, "services": [{"type": "45-min priv training", "available_times": [time of day - Monday]]} 
                    "non_availability":  # time ranges not available
                }
                candlesticks.append(candlestick)
        
        print(f'{file_path} parse complete')
    
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    
    return trainer_list


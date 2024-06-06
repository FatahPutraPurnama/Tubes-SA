import pandas as pd

class Flight:
    def __init__(self, start, end, departure, arrival, duration, distance, price):
        self.start = start
        self.end = end
        self.departure = departure  # already in minutes
        self.arrival = arrival      # already in minutes
        self.duration = duration    # duration in minutes
        self.distance = distance
        self.price = price

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_hhmm(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}"

def load_flights(filename):
    df = pd.read_csv(filename)
    print("Loaded columns:", df.columns.tolist())  # Cetak nama kolom yang dimuat
    flights = []
    for _, row in df.iterrows():
        duration = float(row['Flight Duration'].split()[0]) * 60  # Mengonversi durasi ke menit
        flights.append(Flight(row['Origin'], row['Destination'], time_to_minutes(row['Departure Time']), 
                              time_to_minutes(row['Arrival Time']), duration, row['Distance (km)'], row['Price']))
    return flights

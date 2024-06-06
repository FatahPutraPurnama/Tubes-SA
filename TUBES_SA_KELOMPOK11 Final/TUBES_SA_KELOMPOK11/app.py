from flask import Flask, render_template, request, redirect, url_for
from flight import Flight, time_to_minutes, minutes_to_hhmm, load_flights
from dijkstra import dijkstra
from branch_and_bound import branch_and_bound

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate, minutes_to_hhmm=minutes_to_hhmm)  # Make enumerate and minutes_to_hhmm available in Jinja2 templates

# Gunakan raw string dengan r prefix untuk menghindari unicode escape error
flights = load_flights(r'C:\Users\rikyy\OneDrive\Documents\TUBES_SA_KELOMPOK11\flight_schedule.csv')

@app.route('/')
def index():
    return render_template('index.html', flights=flights)

@app.route('/find_best', methods=['POST'])
def find_best():
    selected_flight_indices = request.form.getlist('selected_flights')

    selected_flights = [flights[int(index)] for index in selected_flight_indices]

    # Menentukan kota asal dan tujuan dari penerbangan yang dipilih
    if not selected_flights:
        return redirect(url_for('index'))

    start_city = selected_flights[0].start
    end_city = selected_flights[-1].end

    dijkstra_result, dijkstra_time = dijkstra(selected_flights, start_city, end_city)
    bb_result, bb_time = branch_and_bound(selected_flights, start_city, end_city)

    return render_template('results.html', 
                           dijkstra_result=dijkstra_result, dijkstra_time=dijkstra_time,
                           bb_result=bb_result, bb_time=bb_time)

if __name__ == '__main__':
    app.run(debug=True)

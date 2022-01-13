from flask import Flask, render_template    # сперва подключим модуль
from flask_debugtoolbar import DebugToolbarExtension, toolbar
import data

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/departures/<departure>/')
def show_departures(departure):
    return render_template('departure.html')

@app.route('/tours/<id>/')
def show_tours(id):
    return render_template('tour.html')

@app.route('/data/')
def show_data_all():
    s_out = render_template('data_all.html')
    for k, v in data.tours.items():
        s_out += render_template('data_tour.html', country=v["country"], key=k, hotel=v["title"], price=v["price"], stars=v["stars"])
    return s_out

@app.route('/data/departures/<departure>/')
def show_data_departure(departure):
    departure_value = departure.lower()
    if departure_value not in data.departures:
        return render_template('data_tours.html', direction=departure, not_found=" не найдены")
    s_out = render_template('data_tours.html', direction=data.departures[departure_value])
    for k, v in data.tours.items():
        if v["departure"] == departure_value:
            s_out += render_template('data_tour.html', country=v["country"], key=k, hotel=v["title"], price=v["price"], stars=v["stars"])
    return s_out

@app.route('/data/tours/<int:id>/')
def show_data_hotel(id):
    if id not in data.tours:
        return render_template('data_tours.html', direction=id, not_found=" не найдены")
    v = data.tours[id]
    return render_template('data_hotel.html', country=v["country"], hotel=v["title"], price=v["price"], nights=v["nights"], description=v["description"])

toolbar = DebugToolbarExtension(app)
app.run(debug=True)    # ('0.0.0.0',8000,debug=True)    # запустим сервер на 8000 порту!
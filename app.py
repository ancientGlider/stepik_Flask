from flask import Flask, render_template    # сперва подключим модуль
from random import choice
import data

app = Flask(__name__)      # объявим экземпляр фласка

def return_error():
    pass

@app.route('/')
def main_page():
    def choice_tours():
        res = {}
        l = list(data.tours)
        while len(res) < 6 and len(res) < len(l):
            tour_number = choice(l)
            res[tour_number] = data.tours[tour_number]
        return res
    return render_template('index.html', departures=data.departures, tours=choice_tours())

@app.route('/departures/<departure>/')
def show_departures(departure):
    if departure in data.departures:
        return render_template('departure.html', departures=data.departures,
                               tours={k: v for k, v in data.tours.items() if v["departure"] == departure},
                               departure=departure)
    else:
        return render_template('oops.html', departures=data.departures), 400

@app.route('/tours/<id>/')
def show_tours(id):
    try:
        id = int(id)
    except Exception:
        pass
    if id in data.tours:
        return render_template('tour.html', departures=data.departures, departure=data.tours[id]["departure"],
                               tour=data.tours[id])
    else:
        return render_template('oops.html', departures=data.departures)

@app.route('/buy/<price>/')
def show_purchase(price):
    if price.isdigit():
        return render_template('payment.html', departures=data.departures, price=price)
    else:
        return render_template('oops.html', departures=data.departures)

app.run('0.0.0.0', 5001, debug=False)
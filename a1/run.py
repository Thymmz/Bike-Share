# Atharva Deshpande, ad3756@drexel.edu
# CS530: DUI, Assignment 1

from flask import Flask, render_template, send_file
import os

data =  [{
        "id": "b1",
        "name": "Sixthreezero Around The Block Women's Single Speed Cruiser Bicycle Coral w/ Black Seat/Grips",
        "wheels": 2,
        "size": 26,
        "motor": "No",
        "folding": "No",
        "image": "sixthreezero.jpg",
        "available": 2
    },
    {
        "id": "b2",
        "name": "Roadmaster 26 Men's Granite Peak Men's Bike",
        "wheels": 2,
        "size": 26,
        "motor": "No",
        "folding": "No",
        "image": "roadmaster.jpg",
        "available": 0
    },
    {
        "id": "b3",
        "name": "Fun 20 Inch Wheel Unicycle with Alloy Rim",
        "wheels": 1,
        "size": 20,
        "motor": "No",
        "folding": "No",
        "image": "unicycle.jpg",
        "available": 7
    },
    {
        "id": "b4",
        "name": "Mongoose Dolomite Fat Tire Mountain Bike",
        "wheels": 2,
        "size": 26,
        "motor": "No",
        "folding": "No",
        "image": "mongoose.jpg",
        "available": 3
    },
    {
        "id": "b5",
        "name": "EuroMini ZiZZO Campo 28lb Lightweight Aluminum Frame Shimano 7 - Speed Folding Bike",
        "wheels": 2,
        "size": 20,
        "motor": "No",
        "folding": "Yes",
        "image": "euromini.jpg",
        "available": 1
    },
    {
        "id": "b6",
        "name": "Huffy Mountain Bike Summit Ridge w / Shimano & Trail Tires",
        "wheels": 2,
        "size": 24,
        "motor": "No",
        "folding": "No",
        "image": "huffy.jpg",
        "available": 0
    },
    {
        "id": "b7",
        "name": "Razor RSF350 Electric Street Bike",
        "wheels": 2,
        "size": 10,
        "motor": "Yes",
        "folding": "No",
        "image": "razor.jpg",
        "available": 8
    },
    {
        "id": "b8",
        "name": "Shaofu Folding Electric Bicycle – 350W 36V Waterproof E-Bike with 15 Mile Range Collapsible Frame and APP Speed Setting",
        "wheels": 2,
        "size": 12,
        "motor": "Yes",
        "folding": "Yes",
        "image": "shaofu.jpg",
        "available": 0
    },
    {
        "id": "b9",
        "name": "Goplus Adult Tricycle Trike Cruise Bike Three-Wheeled Bicycle w/Large Size Basket for Recreation Shopping Exercise",
        "wheels": 3,
        "size": 26,
        "motor": "No",
        "folding": "No",
        "image": "tricycle.jpg",
        "available": 2
    },
    {
        "id": "b10",
        "name": "Swagtron 200W SWAGCYCLE Envy Steel Frame Folding Electric Bicycle e Bike w / Automatic Headlight",
        "wheels": 2,
        "size": 12,
        "motor": "Yes",
        "folding": "Yes",
        "image": "swagtron.jpg",
        "available": 5
    }]


app = Flask(__name__, static_folder='public', static_url_path='')


# Handle the index (home) page
@app.route('/')
def index():
    return render_template('index.html')


# Handle any files that begin "/course" by loading from the course directory
@app.route('/course/<path:path>')
def base_static(path):
    return send_file(os.path.join(app.root_path, '..', 'course', path))


# Handle any unhandled filename by loading its template
@app.route('/<name>')
def generic(name):
    return render_template(name + '.html')


# Any additional handlers that go beyond simply loading a template
# (e.g., a handler that needs to pass data to a template) can be added here
@app.route('/ourbikes')
def bikes():
    return render_template('ourbikes.html', len = len(data), data = data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

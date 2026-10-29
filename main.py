from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/api/v1/position/<s0>/<s1>/<e0>/<e1>/<progress>', methods=['GET'])
def get_position(s0, s1, e0,  e1, progress):

    lat = float(s0) + (float(e0) - float(s0)) * float(progress)

    lng = float(s1) + (float(e1) - float(s1)) * float(progress)

    return jsonify([lat, lng])


@app.route('/')
def countries():
    return render_template('countries/index.html')



if __name__ == '__main__':
    app.run(debug=True)

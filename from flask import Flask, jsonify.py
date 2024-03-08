from flask import Flask, jsonify

app = Flask('_name_')

@app.route('/person')
def get_person():
    person_data = {
        'name': 'John Doe',
        'age': 30,
        'height': 175,
        'studies': 'Computer Science'
    }
    return jsonify(person_data)

if '_name_' == '_main_':
    app.run(debug=True)
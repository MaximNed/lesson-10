import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    text = "<pre>" + "".join([f'{c["name"]}\n{c["position"]}\n{c["skills"]}\n\n' for c in candidates]) + "</pre>"
    return text


@app.route('/candidates/<int:x>')
def check_candidat(x):
    candidate = {}
    for c in candidates:
        if c['id'] == x:
            candidate = c
            break
    if candidate:
        return f"<img src=\"{candidate['picture']}\"><pre>{candidate['name']}\n{candidate['position']}\n{candidate['skills']}</pre>"

    return '<h1> Таких сотрудников нет </h1>'
    

@app.route('/skills/<x>')
def skills(x):
    candidates_with_skill = [f'{c["name"]}\n{c["position"]}\n{c["skills"]}\n\n' for c in candidates if x.lower() in c['skills'].split(', ') ]
    if candidates_with_skill:
        return "<pre>" + "".join(candidates_with_skill) + "</pre>"
    return 'Сотрудников с данным навыком нет.'


if __name__ == '__main__':
    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = json.load(f)
        for c in candidates:
            c['skills'] = c['skills'].lower() # перевел все скилы в нижний регистр для удобного поиска
    app.run(debug=True)
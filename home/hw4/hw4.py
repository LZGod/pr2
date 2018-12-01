from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'results.csv'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/thanks', methods=['POST'])
def csv_save():
    if request.method == 'POST':
        ask = request.form['ask']
        que1 = request.form['que1']
        que2 = request.form['que2']
        age = request.form['age']
        name = request.form['name']
        surname = request.form['surname']
        form = 'Благодарим за участие в опросе!'
        fieldnames = ['ask', 'que1', 'que2', 'age', 'name', 'surname']
        with open(filename, 'a+', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'ask': ask, 'que1': que1, 'que2': que2, 'age': age,
                             'name': name, 'surname': surname})
        return render_template('thanks.html', form=form)

@app.route('/stats')
def stats_show():
    with open(filename, 'r', encoding='utf-8') as content:
        content = csv.reader(content)
        return render_template('stats.html', content=content)

@app.route('/json')
def json_make():
    dict_csv = {}
    fieldnames = ['ask', 'que1', 'que2', 'age', 'name', 'surname']
    with open(filename, 'r+', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            name = row['name'] + ' ' + row['surname']
            dictcsv[name] = json.loads(json.dumps(row))
    return render_template('json.html', json=dictcsv)

@app.route('/search')
def search_do():
    return render_template('search.html')

@app.route('/result', methods=['POST'])
def result_show():
    dict_csv = {}
    if request.method == 'POST':
        ask = request.form['ask_search']
        what = request.form['what_search']
        fieldnames = ['ask', 'que1', 'que2', 'age', 'name', 'surname']
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                if row['ask'] == ask:
                    if (row['name'] == name
                        or row['surname'] == surname):
                        name = row['name'] + ' ' + row['surname']
                        dictcsv[name] = json.loads(json.dumps(row))
        return render_template('result.html', result=dictcsv)

if __name__ == '__main__':
    app.run(debug=True)

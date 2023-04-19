from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru India',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Remote ',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'San Franciscio, USA',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Franciscio, USA',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='LSP')


@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

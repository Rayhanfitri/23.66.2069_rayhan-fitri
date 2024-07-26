from flask import Flask, render_template
from fp_growth import run_fp_growth

app = Flask(__name__)

@app.route('/')
def index():
    itemsets = run_fp_growth()
    return render_template('index.html', itemsets=itemsets)

if __name__ == '__main__':
    app.run(debug=True)

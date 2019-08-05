from flask import Flask, render_template, make_response
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('matplotlib.html')
   
if __name__ == '__main__':
   app.run(debug = True)
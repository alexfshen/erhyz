import os
from flask import Flask, render_template

#################

directory_path = '/home/fang.shen@Digital-Grenoble.local/Documents/Dev Web/ollama/static/images'
files = os.listdir(directory_path)


################

app = Flask(__name__)

@app.route('/')
def gallery() :
    my_images = files
    my_image = '1.jpg'
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

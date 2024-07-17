#import

import os
from flask import Flask, render_template
import ollama
import glob

#get the list of images

urls = glob.glob('static/images/*.jpg')

#ask ollama to create stories

def generate_stories(urls) :
    query = """
    Can you write a story for kids inspired by the picture?
    """
        
    res = ollama.chat(
        model = "llava",
        messages = [
            {
                'role' : 'user',
                'content' : query,
                'imagines' : [urls]
            }
        ]
    )

    return res['message']['content']


#ask Flask to display

app = Flask(__name__)

stories_python = []

@app.route('/')
def gallery() : 
    for url in urls :
        story = generate_stories(url)
        stories_python.append( (story, url) )
    
    return render_template('gallery2.html', stories=stories_python)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

  
#import

import os
from flask import Flask, render_template
import ollama

#get the list of images

directory_path = '/home/fang.shen@Digital-Grenoble.local/Documents/Dev Web/ollama/static/images'
images = os.listdir(directory_path)

#ask ollama to create stories

def generate_stories(images) :
    images_stories = {}
    for image in images :
        image_path = os.path.join (directory_path, image)
        response = ollama.chat(
            model = "llava",
            messages = [
                {
                    'role' : 'user',
                    'content' : 'Create a story based on this image :',
                    'imagines' : [image_path]
                }
            ]
        )
        story = response['message']['content']

    images_stories[image] = story
    return images_stories

images_stories = generate_stories(images)

#ask Flask to display

app = Flask(__name__)

@app.route('/')
def gallery() : 
        
        return render_template('gallery2.html', images_stories)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

  
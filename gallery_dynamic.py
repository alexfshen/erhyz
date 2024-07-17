import os
from flask import Flask, render_template
import ollama

#################

directory_path = '/home/fang.shen@Digital-Grenoble.local/Documents/Dev Web/ollama/static/images'
files = os.listdir(directory_path)


###########################################


############################################
def generate_stories(images) :
    stories = []
    for image in images :
        image_path = os.path.join(directory_path, image)
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
        stories.append(story)
    return stories

##########################################

app = Flask(__name__)

@app.route('/')
def gallery() :
    try : 
        image_stories = generate_stories(files)
        data = [{'image' : image, 'story' : story} for story in zip(files, image_stories)]
        return render_template('gallery2.html', data = data)
    except Exception as e:
        print(f"Error in gallery route: {str(e)}")
        return "An error occurred while processing images and stories."

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

  
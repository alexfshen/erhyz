import ollama

response = ollama.chat(
    model = "llava",
    messages = [
        {
            'role' : 'user',
            'content' : 'Create a story based on this image :',
            'imagines' : ['./1.jpg']
        }
    ]
)

print (response['message']['content'])

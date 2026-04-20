from flask import Flask, render_template
import json
import os

app = Flask(__name__)

files = {}

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "projects")
projectsfile = os.listdir(file_path)

if os.path.exists(file_path):
    for f in range(len(projectsfile)):
        if os.path.isfile(os.path.join(file_path, projectsfile[f])):

            fi = os.path.join(script_dir, f"projects\{projectsfile[f]}")
            name = "hi"

            with open(fi, "r", encoding="UTF-8") as file:
                files[projectsfile[f].replace(".json","")] = json.load(file)

    # file = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]

else:
    print(f"Папка {file_path} не найдена")
    files = []

with open("projects.json", "r", encoding="UTF-8") as f:
    projects = json.load(f)

print(str(files))

@app.route('/')
def index():
    return render_template('index.html', data={"projects":projects,"projectsCrads":files})

if __name__ == '__main__':
    app.run(debug=True)


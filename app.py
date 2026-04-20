from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__)

files = {}
script_dir = os.path.dirname(os.path.abspath(__file__))

projects_dir = os.path.join(script_dir, "projects")

if os.path.exists(projects_dir) and os.path.isdir(projects_dir):
    for filename in os.listdir(projects_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(projects_dir, filename)  
            try:
                with open(filepath, "r", encoding="UTF-8") as file:
                    key = filename.replace(".json", "")
                    files[key] = json.load(file)
            except Exception as e:
                print(f"Ошибка загрузки {filename}: {e}", flush=True)
else:
    print(f"Папка {projects_dir} не найдена", flush=True)

projects_json_path = os.path.join(script_dir, "projects.json")  
try:
    with open(projects_json_path, "r", encoding="UTF-8") as f:
        projects = json.load(f)
except FileNotFoundError:
    print(f"Файл {projects_json_path} не найден", flush=True)
    projects = [] 

print(f"Загружено проектов: {len(projects)}, карточек: {len(files)}", flush=True)

@app.route('/')
def index():
    return render_template('index.html', data={"projects": projects, "projectsCrads": files})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    application = app
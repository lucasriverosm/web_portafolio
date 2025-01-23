from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            'name': 'Proyecto 1',
            'description': 'Descripción del proyecto 1',
            'technologies': ['Python', 'Flask', 'SQLAlchemy']
        },
        {
            'name': 'Proyecto 2',
            'description': 'Descripción del proyecto 2',
            'technologies': ['JavaScript', 'React', 'Node.js']
        }
    ]
    
    skills = ['Python', 'JavaScript', 'HTML/CSS', 'SQL', 'Git']
    
    return render_template('home.html', 
                         projects=projects,
                         skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
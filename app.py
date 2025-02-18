from flask import Flask, render_template, request

app = Flask(__name__)

# Subject details (name, weightage)
subjects = [
    ("SOFTWARE ENGINEERING BCS501", 4),
    ("COMPUTER NETWORKS BCS502", 4),
    ("THEORY OF COMPUTATION BCS503", 4),
    ("DATA VISUALIZATION LAB", 1),
    ("ARTIFICIAL INTELLIGENCE B515b", 3),
    ("MINI PROJECT B586", 2),
    ("RESEARCH METHODOLOGY B557", 3),
    ("ENVIRONMENTAL SCIENCE (EVS) B508", 1),
]

def calculate_gpa(marks_list):
    total_weightage = sum(weight for _, weight in subjects)
    total_points = sum((min((int(marks) // 10) + 1, 10)) * weight for marks, (_, weight) in zip(marks_list, subjects))
    return round(total_points / total_weightage, 2) if total_weightage else 0

@app.route('/', methods=['GET', 'POST'])
def index():
    gpa = None
    if request.method == 'POST':
        marks = request.form.getlist('marks')
        gpa = calculate_gpa(marks)
    
    return render_template('index.html', subjects=subjects, gpa=gpa)

if __name__ == '__main__':
    app.run(debug=True)

# HTML file: templates/index.html

index_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>GPA Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        form { display: inline-block; margin-top: 20px; }
        input { margin: 5px; padding: 8px; }
        button { padding: 10px; background-color: blue; color: white; border: none; }
    </style>
</head>
<body>
    <h1>GPA Calculator</h1>
    <form method="post">
        {% for subject, weight in subjects %}
            <label>{{ subject }} (Weight: {{ weight }})</label>
            <input type="number" name="marks" min="0" max="100" required><br>
        {% endfor %}
        <button type="submit">Calculate GPA</button>
    </form>
    {% if gpa is not none %}
        <h2>Your GPA: {{ gpa }}</h2>
    {% endif %}
</body>
</html>
'''

# Save HTML file
with open("templates/index.html", "w") as f:
    f.write(index_html)

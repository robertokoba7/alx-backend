from flask import Flask, render_template
"""
create a new Flask app
"""
app = Flask(__name__)

@app.route('/')
def index():
    """
    render the index.html template
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

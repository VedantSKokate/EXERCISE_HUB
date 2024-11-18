from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the welcome page
@app.route('/')
def welcome_page():
    return render_template('welcomepage.html')

# Route for page 1 that shows activities
@app.route('/page1')
def page1():
    # Serve the first page
    return render_template('page1.html')

@app.route('/page2')
def page2():
    # Extract parameters from query string
    exercise_name = request.args.get('exercise_name')
    video1_url = request.args.get('video1_url')
    video2_url = request.args.get('video2_url')

    # Redirect to page1 if any parameter is missing
    if not (exercise_name and video1_url and video2_url):
        return redirect(url_for('page1'))

    # Render page2 with the provided parameters
    return render_template(
        'page2.html',
        exercise_name=exercise_name,
        video1_url=video1_url,
        video2_url=video2_url
    )
# Route for page 3 (additional exercises or details)
@app.route('/page3')
def page3():
    return render_template('page3.html')

# Route for page 4 (additional exercises or details)
@app.route('/page4')
def page4():
    return render_template('page4.html')

# Route for page 5 (additional exercises or details)
@app.route('/page5')
def page5():
    return render_template('page5.html')

# Route for specific activities page (e.g., gym exercise details)
@app.route('/page6/<exercise_name>')
def page6(exercise_name):
    return render_template('page6.html', exercise_name=exercise_name)

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)

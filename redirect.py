'''Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the 
working of the url_for() function.'''


from flask import Flask, url_for, redirect

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route for the about page
@app.route('/about')
def about():
    return "This is the About Page."

# Route to demonstrate redirection using url_for
@app.route('/go-to-about')
def go_to_about():
    # Use url_for to generate the URL for 'about' and redirect
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)
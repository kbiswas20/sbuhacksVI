from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'user_id' in session:
        return render_template('home.html', username=session['user_id'])
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = request.form.get('username')
        return redirect(url_for('home'))  # Redirect to home page after dummy login

    return render_template('login.html')  # Render login page

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session['user_id'] = request.form.get('username')
        return redirect(url_for('home'))  # Redirect to home page after dummy signup

    return render_template('signup.html')  # Render signup page

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Here you could process the form data, such as sending an email

    # If GET request, render the contact form
    return render_template('contact.html')

@app.route("/search", methods=['GET'])
def search():
    search_query = request.args.get('q', '')
    # Here you can process the search_query as needed
    return render_template('search_results.html', query=search_query)

@app.route("/science", methods=['GET'])
def science_page():
    return render_template('science.html')

if __name__ == '__main__':
    app.run(debug=True)

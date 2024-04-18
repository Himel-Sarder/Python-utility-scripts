from flask import Flask, redirect, request
import random
import string

app = Flask(__name__)
url_database = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

@app.route('/')
def index():
    return "Welcome to URL Shortener!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    short_url = generate_short_url()
    url_database[short_url] = long_url
    return f"Shortened URL: {request.host}/{short_url}"

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found!"

if __name__ == '__main__':
    app.run(debug=True)

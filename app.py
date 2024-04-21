# Import necessary libraries
from flask import Flask, redirect, url_for, request, render_template, session
from pytube import YouTube  # Import YouTube module from pytube for downloading YouTube videos
import os  # Import os module for interacting with the operating system
import requests  # Import requests module for making HTTP requests

app = Flask(__name__)  # Create a Flask web application instance

# Define a route for the root URL (Homepage)
@app.route('/', methods=['GET'])  # This route handles GET requests to the root URL
def index():
    # When a GET request is received, render the index.html template
    return render_template('index.html')

# Define a route for the root URL (Homepage) but for POST requests
@app.route('/', methods=['POST'])  # This route handles POST requests to the root URL
def index_post():
    # Retrieve the text input from the submitted form
    yt = request.form['text']
    
    # Create a YouTube object using the pytube library
    yt = YouTube(yt)
    
    # Get the first available stream that contains only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # Define the destination folder for the downloaded file
    destination = '.'
    
    # Download the video to the specified output path
    out_file = video.download(output_path=destination)
    
    # Split the downloaded file path into base and extension
    base, ext = os.path.splitext(out_file)
    
    # Create a new file path by changing the extension to .mp3
    new_file = base + '.mp3'
    
    # Rename the downloaded file to the new .mp3 file
    os.rename(out_file, new_file)
    
    # Render the results.html template (currently without passing any data)
    return render_template('results.html')

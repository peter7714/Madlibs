from flask import Flask, render_template, request
from flask_debugtoolbar import debugToolbarExtension
from stories import story 

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = debugToolbarExtension(app)

@app.route('/')
def ask_questions():
    """Generates a form for user to input words"""

    prompts = story.prompt

    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Show Madlib"""
    text = story.generate(request.args)

    return render_template('story.html', text =text)
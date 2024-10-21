#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import string
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

@app.route('/generate_password')
def generate_password():
    # Get length from form input (via query parameters)
    lt = request.args.get('length', default=8, type=int)

    # Ensure password length is between 8 and 16
    if lt < 8:
        lt = 8
    elif lt > 16:
        lt = 16

    # Characters to be included in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # Concatenate all the characters
    L = lower + upper + num + symbols

    # Generate a random password
    pw = random.sample(L, lt)
    password = "".join(pw)

    # Render the template with the generated password
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





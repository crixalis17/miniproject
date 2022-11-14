from flask import Flask, render_template, request, jsonify 
from flask import request 
import time
import pandas as pd

from enigma.preprocessing import preprocess_tweets
from enigma.output import final_output
from enigma.bert_tokenizer import tokenize
from rylai.scrape import webscrape

app = Flask(__name__) 

df_dict = {
    'Name': 'Ramesh',
	'tweets': 10,
	'bullying': 5,
	'percentage':50.00
  }

def bert_output(website_url): 
	profile_name = webscrape(website_url)
	preprocess_tweets()
	final_output(profile_name,tokenize)
	return df_dict

@app.route('/')
def input():
    return render_template('index.html')
    

@app.route('/passing', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        website = str(request.form['name'])
        print("WEBSITE_URL = ",website)
        
        result = bert_output(website)

        # Send result data to result_data HTML file
        return render_template("temp.html", result=result)
  
 
if __name__ == '__main__': 
	app.run(debug=True) 
''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis import sentiment_analyzer
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO

#Initiate the flask app : TODO
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    txt = request.args['textToAnalyze']
    if txt == '':
        return 'No text provided !'
    rsp = sentiment_analyzer(txt)
    label = rsp['label']
    score = rsp['score']
    if label is None or score is None:
        return 'Invalid input ! Try again.'
    return f'The given text has been identified as {label} with a score of {score}.'

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

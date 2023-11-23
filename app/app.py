from flask import Flask,render_template,url_for,request
import os
import joblib


# ML Packages
news_vectorizer = open(os.path.join("static/models/final_news_cv_vectorizer.pkl"),"rb")
news_cv = joblib.load(news_vectorizer)


app = Flask(__name__)

def get_keys(val,my_dict):
	for key,value in my_dict.items():
		if val == value:
			return key 


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
	# Receives the input query from form
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		modelchoice = request.form['modelchoice']
		vectorized_text = news_cv.transform([rawtext]).toarray()
		
		if modelchoice == 'nb':
			news_nb_model = open(os.path.join("static/models/newsclassifier_NB_model.pkl"),'rb')
			news_clf = joblib.load(news_nb_model)
		elif modelchoice == 'logit':
			news_nb_model = open(os.path.join("static/models/newsclassifier_Logit_model.pkl"),'rb')
			news_clf = joblib.load(news_nb_model)
		elif modelchoice == 'rf':
			news_nb_model = open(os.path.join("static/models/newsclassifier_RFOREST_model.pkl"),'rb')
			news_clf = joblib.load(news_nb_model)

		#Prediction
		prediction_labels = {"business":0,"tech":1,"sport":2,"health":3,"politics":4,"entertainment":5}
		prediction = news_clf.predict(vectorized_text)
		final_result = get_keys(prediction,prediction_labels)

	
	return render_template('index.html',final_result=final_result ,rawtext = rawtext.upper())



if __name__ == '__main__':
	app.run(debug=True)
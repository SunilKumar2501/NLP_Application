import requests

class API:
	def __init__(self):
		self.querystring = None
		self.string = None
		self.headers = {
			"x-rapidapi-key": "9fde98c4c2mshce9debf60b79934p1aa736jsne4a055ad9d42",
			"x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com" }
		self.headers1 = {
		"x-rapidapi-key": "9fde98c4c2mshce9debf60b79934p1aa736jsne4a055ad9d42",
		"x-rapidapi-host": "text-to-emotions2.p.rapidapi.com" }

	def sentiment_analysis(self,text):
		self.querystring = {"text": text}
		url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"
		response = requests.get(url, headers=self.headers, params=self.querystring)
		return response.json()

	def emotional_detection(self,text):
		url2 = "https://text-to-emotions2.p.rapidapi.com/predict-emotions"
		header2 = {	"x-rapidapi-key": "9fde98c4c2mshce9debf60b79934p1aa736jsne4a055ad9d42",
		"x-rapidapi-host": "text-to-emotions2.p.rapidapi.com",
		"Content-Type": "application/json"
		}
		# Prepare the data to be sent in the request body
		data = {
			"text": text
		}
		# Make the POST request to the API
		response = requests.post(url2, headers=header2, json=data)

		# Print the response in JSON format
		return response.json()











		# string = {"prediction":"I am sad"}
		# url1 = "https://text-to-emotions2.p.rapidapi.com/predict-emotions/:%7Btext%7D"
		#
		# response = requests.get(url1, headers=self.headers1,params = string)
		#
		#
		# print(response.json())



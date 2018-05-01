import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('s.json') as json_data:
    d = json.load(json_data)
    list_of_food = []
    for data in d['food']:
    	list_of_food.append(data)


@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/food', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_food)

@app.route('/food/<string:idd>', methods =['GET'])
def test2(idd):
	g = [food for food in list_of_food if food['id'] == idd]
	return render_template("index.html",list_data=g)

if __name__ == '__main__':
	 app.run(host='0.0.0.0')
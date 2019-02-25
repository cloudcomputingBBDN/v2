from flask import Flask, request,jsonify
from flask_restful import Resource, Api,reqparse,abort
import json
app = Flask(__name__)
api = Api(app)
import time
import csv

parser = reqparse.RequestParser()
from flask import make_response


class ListAll(Resource):
	def get(self):
		l={}
		with open('t.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				l[row[0]] = int(row[1])		
		return jsonify(l)    




	def post(self):
		json_data = request.get_json(force=True)
		parser.add_argument('name', type=str, location='json')
		print(type(json_data['name']))
		time.sleep(1)
		data=json_data['name']
		print(type(data))
		print(data)
		time.sleep(10)
		aa=len(data)
		with open('t.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			flag=0
			for row in csv_reader:
				if(row[0]==data[0]):
					flag=1
				if(flag==1):
					return make_response(jsonify({'error':'Bad request,Entry already exists'}),400)
		if(aa>1):
			return make_response(jsonify({'error':'Bad request,Length of input exceeded,multiple categories canoot be added at a time'}),400)
		with open('t.csv', 'a') as csvFile:
			writer = csv.writer(csvFile)
			r=[data,0]
			writer.writerow(r)
		return jsonify({}), 201 




api.add_resource(ListAll, '/api/v1/categories')






if __name__ == '__main__':
    app.run(debug=True)


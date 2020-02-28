import pickle
import traceback
import json

from flasgger import Swagger
from flask import Flask, request, jsonify


app = Flask(__name__)


swagger_config = {
   "headers": [
   ],
   "specs": [
       {
           "endpoint": 'apispec_1',
           "route": '/apispec_1.json',
           "rule_filter": lambda rule: True, 
           "model_filter": lambda tag: True,
       }
   ],
   "static_url_path": "/flasgger_static",
   "swagger_ui": True,
   "specs_route": "/api/v1"
}


template = {
 "swagger": "2.0",
 "info": {
   "title": "My ML API",
   "description": "An API to offer the predict functionality of a ML model",
   "contact": {
     "responsibleOrganization": "MyOrganization",
     "responsibleDeveloper": "Me",
     "email": "me@me.com",
     "url": "www.me.com",
   },
   "termsOfService": "http://me.com/terms",
   "version": "0.0.1"
 }
}

swagger = Swagger(app, template=template, config=swagger_config)

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    """Endpoint used for serving the prediction function of the ML model
    
    Get a prediction for given input

    ---
    parameters:
      - name: input parameter 
        in: formData
        type: json
        required: true
        description: Data-in for prediction
    responses:
      200:
        description: Prediction
        examples: {"prediction": true, "confidence": true}

    """
    response = dict()
    
    # Ensure an image was properly uploaded to our endpoint.
    if request.method == 'POST':
        
		# digest request.text or request.stream and transform into required format
		# >>> input = json.loads(request.txt)

		# use loaded model to create prediction
		# >>> prediction = model.predict(input)

        # Compile response object
        response["prediction"] = prediction

            
    # Return the data dictionary as a JSON response.
    return jsonify(response)

if __name__ == '__main__':
    try:
		with open('relative/path/to/binary/modelfile.pkl', 'rb') as fp:	
			model = pickle.load(fp)
			
        print('model loaded')
        
            
    except Exception as e:
        raise ValueError('No model here')

app.run(host="0.0.0.0", port=5000, debug=True)

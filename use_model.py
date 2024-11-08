import xgboost as xgb
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = "model_xgb.bin"
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():
    adult = request.get_json()
    
    X_adult = dv.transform([adult])
    features = list(dv.get_feature_names_out())
    dval = xgb.DMatrix(X_adult, feature_names=features)

    y_pred = model.predict(dval)
    income = y_pred >= 0.5
    result = {
        "Probability that this adult has anual income >50k": float(y_pred),
        "income >50k": bool(income)
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)
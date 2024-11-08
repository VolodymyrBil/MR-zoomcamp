import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import xgboost as xgb

import pickle


from ucimlrepo import fetch_ucirepo 

random_state = 1

#dowloading dataset from web
'''
adult = fetch_ucirepo(id=2) 
print("Dataset downloaded successfully")

df = adult.data.features 
df['y'] = adult.data.targets '''

# or just dowload dataset form file
df = pd.read_csv('adult_income.csv')

#data preparation
df.columns = df.columns.str.lower().str.replace('-', '_')
df.columns = df.columns.str.lower().str.replace(' ', '_')

df = df.fillna("")
df.workclass = df.workclass.replace('?', '')
df.occupation = df.occupation.replace('?', '')

df['y']  = ((df['y'] == '>50K') | (df['y'] == '>50K.')).astype(int)

#spliting the data. I will use df_full_train for training here
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=random_state)
#df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=random_state)
assert len(df) == (len(df_full_train) + len(df_test))

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_test = df_test.y.values
y_full_train = df_full_train.y.values

del df_full_train['y']
del df_test['y']

dv = DictVectorizer(sparse=True)
full_train_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(full_train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)

features = list(dv.get_feature_names_out())
dtrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

watchlist = [(dtrain, 'train'), (dtest, 'test')]

eta=0.1
max_depth = 6
min_child_weight = 1
num_boost_round = 130

xgb_params = {
    'eta': eta, 
    'max_depth': max_depth,
    'min_child_weight': min_child_weight,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, evals = watchlist, num_boost_round=num_boost_round)
print("Model trained successfully")

output_file = "model_xgb.bin"
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print("Model saved to file %s successfully"%output_file)


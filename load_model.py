import joblib
model = joblib.load('diabetic_79.pkl')
result = model.predict([[1, 1, 1, 1, 1, 1, 1, 1]])
# print(result)

if result[0]==1:
    print('person is diabetic')
else:
    print('person is not diabetic')
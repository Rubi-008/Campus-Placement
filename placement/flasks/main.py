from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

model = pickle.load(open(r"C:\Users\ITPARKCOMPUTERS\PycharmProjects\place\placement.pkl", 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():

    x_test = [int(yo) for yo in request.form.values()]
    #ts = [np.array(x_test)]
    prediction = model.predict([x_test])
    #opt = prediction[0]
    return render_template('index.html', y='prediction is {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=False)






from flask import Flask,render_template,request
import numpy as np
import waitress as server
app = Flask(__name__)
@app.route('/liver',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        age = request.form['age']
        sex = request.form['sex']
        total_bilirubin = request.form['chest']
        direct_bilirubin = request.form['trestbps']
        alkaline_phosphotase = request.form['chol']
        alamine_aminotransferase = request.form['fbs']
        aspartate_aminotransferase = request.form['restecg']
        total_proteins = request.form['thalach']
        albumin = request.form['exang']
        albumin_and_globulin_ratio = request.form['oldpeak']

        model1 = pickle.load(open('./static/liver_model.pkl','rb'))
        input_data = (age,sex,total_bilirubin,direct_bilirubin,alkaline_phosphotase,alamine_aminotransferase,aspartate_aminotransferase,total_proteins,albumin,albumin_and_globulin_ratio)
        print(input_data)
        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = model1.predict(input_data_reshaped)
        senddata=""
        if (prediction[0]== 2):
            senddata='According to the given details person does not have Liver Disease'
        else:
            senddata='According to the given details chances of having Liver Disease are High, So Please Consult a Doctor'
        return render_template('homepage2.html',resultvalue=senddata)
    if __name__ == '_main_':
           app.run(debug=True)

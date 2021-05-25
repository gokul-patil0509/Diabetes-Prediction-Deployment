from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np


# Load the Random Forest Classifier Model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

# Diabetes-Prediction-Model

def home(request):
        return render(request,'index.html')


def predict(request):   

    if request.method == 'POST':
        preg = int(request.POST.get('pregnancies'))
        glucose = int(request.POST.get('glucose'))
        bp = int(request.POST.get('bloodpressure'))
        st = int(request.POST.get('skinthickness'))
        insulin = int(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        dpf = float(request.POST.get('dpf'))
        age = int(request.POST.get('age'))

        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        context = {'prediction':my_prediction}
        return render(request,'result.html',context)

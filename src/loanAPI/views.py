import json
import pickle
import joblib

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, request

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

import numpy as np
import pandas as pd
from sklearn import preprocessing

from .forms import MyForm
from .models import Approvals
from .serializers import ApprovalsSerializers

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = ApprovalsSerializers

def myform(request):
    if request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            #myform.save()
    else:
        form = MyForm()

@api_view(["POST"])
def approve_reject(request):
    try:
        model = joblib.load('./research/pickle/loan_model.pkl')
        my_data = request.data
        unit = np.array(list(my_data.values()))
        unit = unit.reshape(1, -1)
        scalers = joblib.load('./research/pickle/scalers.pkl')
        x = scalers.transform(unit)
        y_pred = model.predict(x)
        y_pred = (y_pred > 0.58)
        new_df = pd.DataFrame(y_pred, columns=['Status'])
        new_df = new_df.replace({True: 'Approved', False: 'Rejected'})
        return JsonResponse('Your status is {}'.format(new_df), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 


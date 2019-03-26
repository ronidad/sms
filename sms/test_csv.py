from django.shortcuts import render, redirect
import csv




def upload_csv(request):
    if "GET" == request.method:
        data = csv.DictReader(paramFile)
        return render(request, "sms/upload_csv.html", data)
        paramFile = request.FILES['file'].read()
        data = csv.DictReader(paramFile)
        list1 = []
        for row in data:
            list1.append(row)

        print (list1)

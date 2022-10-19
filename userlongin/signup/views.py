import numbers
from tokenize import Number
from django.shortcuts import render
import mysql.connector as sql
username=''
email=''
number=''
pwd=''
pwd =''
desc = ''

# Create your views here.
def signup(request):
    global username,email,number,pwd
    if request.method == 'POST':
        toSql=sql.connect(host='localhost',user='root',password='',database='xenon')
        cursor=toSql.cursor()
        dataValue = request.POST
        for key, value in dataValue.items():
            if key == 'user1':
                username = value
            if key == 'email':
                email = value
            if key == 'phone':
                number = value
            if key == 'pass1':
                pwd = value
            if key == 'pass2':
                pwd == value
        values = "INSERT INTO users values('{}','{}','{}','{}','{}')".format(username,email,number,pwd,pwd)
        cursor.execute(values)
        toSql.commit()
    return render(request, 'signup/register.html')

def contact(request):
    global enname,desc
    if request.method == 'POST':
        toSql=sql.connect(host='localhost',user='root',password='',database='xanon')
        cursor=toSql.cursor()
        dataValue = request.POST
        for key, value in dataValue.items():
            if key == 'name':
                enname = value
            if key == 'desc':
                desc = value
        values = "INSERT INTO enquiry values('{}','{}')".format(enname,desc)
        cursor.execute(values)
        toSql.commit()
    return render(request, 'contectUsPage.html')
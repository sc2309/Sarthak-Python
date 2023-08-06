from flask import Blueprint, request, render_template
import openpyxl

auth = Blueprint('auth', __name__)

@auth.route('/result', methods=['GET', 'POST'])
def login():
    maths = int(request.form.get('math_marks'))
    science = int(request.form.get('science_marks'))
    eng_hin = int(request.form.get('EngHin_marks'))
    computer = int(request.form.get('Comp_marks'))
    ssc = int(request.form.get('SSC_marks'))
    total = int(request.form.get('total_marks'))
    sum = maths + science + eng_hin + computer + ssc
    head = sum/total 
    head = head * 100
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    data = [
        ["Maths","Science","Eng Hin","Computer","SSc"],
        [maths,science,eng_hin,computer,ssc]
    ]
    for row in data:
        sheet.append(row)
    workbook.save("data.xlsx")
    return render_template('result.html', headtype=head)
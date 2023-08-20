from flask import Blueprint, request, render_template
import openpyxl

auth = Blueprint('auth', __name__)

def StoreData(file_name, data):
    try:
        workbook = openpyxl.load_workbook(file_name)
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(data)
    workbook.save(file_name)

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
    excel_file_name = "data.xlsx"
    marks = [maths, science, eng_hin, computer, ssc]
    StoreData(excel_file_name, marks)
    return render_template('result.html', headtype=head)
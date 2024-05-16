
from flask import Flask, request, jsonify, render_template
import spamFilter
import csv  
app = Flask(__name__)

@app.route('/')
def main_menu():
    return render_template('mainMenu.html')

@app.route('/generalMode')
def index():
    return render_template('generalMode.html')  

@app.route('/selectmode')
def select_mode():
    return render_template('selectmode.html')

@app.route('/businessMode')
def business_mode():
    return render_template('businessMode.html')  

@app.route('/lists')
def lists():
    return render_template('lists.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/scan', methods=['POST'])
def scan_email():
    form_name = request.form.get('form_name')
    email_content = request.form['email_content']
    
    if(form_name == "general_mode"):
        result = spamFilter.is_spam(email_content,"general_mode")
        print("hello2312")
        return render_template('generalMode.html', result=result)  
    
    elif(form_name == "business_mode"):
        result = spamFilter.is_spam(email_content,"business_mode")
        print("asfasfsafasfasfasfsaf")

        return render_template('businessMode.html', result=result)  
    else:
        result = spamFilter.is_spam(email_content,"general_mode")
        print("hello")
        return render_template('generalMode.html', result=result)  




@app.route('/update_black_list', methods=['POST'])
def update_black_list():

    with open('black_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    print("go1")

    word = request.form['add']
    rows.append([word, 100.0])

    with open('black_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return render_template('lists.html')

@app.route('/update_white_list', methods=['POST'])
def update_white_list():

    with open('white_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    word = request.form['remove']
    rows.append([word, -100.0])

    with open('white_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    

    with open('black_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [row for row in rows if row[0] != word]

    with open('black_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)


    return render_template('lists.html')

if __name__ == '__main__':
    app.run(debug=True)

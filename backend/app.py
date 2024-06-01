
from flask import Flask, request, jsonify, render_template
import spamFilter
import csv  
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')


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

@app.route('/commercialMode')
def commercial_mode():
    return render_template('commercialMode.html')
  
@app.route('/dailyMode')
def daily_mode():
    return render_template('dailyMode.html')    

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
    
    if(form_name == "daily_mode"):
        result = spamFilter.is_spam(email_content,"daily_mode")
        return render_template('dailyMode.html', result=result)  
    
    elif(form_name == "business_mode"):
        result = spamFilter.is_spam(email_content,"business_mode")
        return render_template('businessMode.html', result=result)
    
    elif(form_name == "commercial_mode"):
        result = spamFilter.is_spam(email_content,"commercial_mode")
        return render_template('commercialMode.html', result=result)
      
    else:
        result = spamFilter.is_spam(email_content,"general_mode")
        return render_template('generalMode.html', result=result)  

@app.route('/update_black_list', methods=['POST'])
def update_black_list():

    with open('datasets/black_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    word = request.form['add']
    rows.append([word, 100.0])


    with open('datasets/black_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    with open('datasets/white_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [row for row in rows if row[0] != word]

    with open('datasets/white_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    return render_template('lists.html')

@app.route('/update_white_list', methods=['POST'])
def update_white_list():

    with open('datasets/white_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    word = request.form['remove']
    rows.append([word, -100.0])

    with open('datasets/white_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    with open('datasets/black_list.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [row for row in rows if row[0] != word]

    with open('datasets/black_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    return render_template('lists.html')

if __name__ == '__main__':
    app.run(debug=True)

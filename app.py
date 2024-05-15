# from flask import Flask, request, jsonify, render_template
# import spamFilter  # Modelinizi içeren modülü buraya ekleyin

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/scan', methods=['POST'])
# def scan_email():
#     email_content = request.form['email_content']
#     # Modelinizi kullanarak burada e-posta içeriğini işleyin
#     result = spamFilter.is_spam(email_content)
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
import spamFilter  # Modelinizi içeren modülü buraya ekleyin

app = Flask(__name__)

@app.route('/mainMenu')
def main_menu():
    return render_template('mainMenu.html')

@app.route('/generalMode')
def index():
    return render_template('generalMode.html')  # İlk açılış sayfanız

@app.route('/selectmode')
def select_mode():
    return render_template('selectmode.html')

@app.route('/lists')
def lists():
    return render_template('lists.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/scan', methods=['POST'])
def scan_email():
    print(request.method)
    email_content = request.form['email_content']
    result = spamFilter.is_spam(email_content)
    print(type(result))
    return render_template('generalMode.html', result=result)  # Sonuç sayfanızı render edin

if __name__ == '__main__':
    app.run(debug=True)

SpamShield


Project Description:
	"SpamShield" is an application that protects users' email inboxes from spam emails.

Installation:

	1- Installation of Required Software:
		Node.js (https://nodejs.org/en  - version 20.12.2)
		Python (https://www.python.org/ - version 3.10.5)

	2- Downloading and Installing the Project Folder:
		-Clone this repository or download it as a zip file.
  		-Then copy these files into an empty project folder.
		-Navigate to the project folder in your terminal or command prompt.
	
	3- Frontend Installation:
		-Navigate to the frontend folder using the command "cd frontend" in your terminal or command prompt.
		-Then, run the command "npm install electron@30.0.5" to install the Electron.js framework.
	
	4- Backend Installation:
		-Navigate to the backend folder using the command "cd backend" in your terminal or command prompt.
		-Then, run the command "pip install Flask == 3.0.3" to install the Flask framework.
	
	5- Installation of Main Module:
		-Navigate to the backend folder using the command "cd backend" in your terminal or command prompt.
		-Then, run the following commands one by one to install the required libraries:
			* "pip install beautifulsoup4==4.11.1"
			* "pip install numpy==1.23.2"
			* "pip install pandas==1.5.0"
			* "pip install scikit-learn==1.2.2"
			* "pip install nltk==3.8.1"
			* "pip install openpyxl==3.1.2"

Usage:

	Starting the Application:
		-Navigate to the backend folder using the command "cd backend" in your terminal or command prompt.
		-Run the command "python app.py" to start the application.
		-Then, open the URL link shown in the console in your web browser. (http://127.0.0.1:5000)
	
	Using the Application:
		-When the application opens, you can run your email in the appropriate mode.
		-If you are unsure which mode to choose, you can select the general mode.
		-By adding a word to the blacklist, if that word is encountered in future emails, you will receive a direct spam response.
		-By adding a word to the whitelist, if future emails are marked as spam and it is due to that word, the word will be ignored.

License:

	This project is licensed under the MIT License. See the LICENSE file for more information.


Contact:
	Team: Team 5
	GitHubs: https://github.com/canertunc, https://github.com/cemregonenc, https://github.com/fethiyesari, https://github.com/Halilakca17, https://github.com/ibrahimbinbuga, 			https://github.com/muratakdere
	Email: canertunc982@gmail.com
	More Detail About Project: https://muratakdere.github.io/SpamShield/

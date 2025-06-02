# SpamShield - Advanced Email Spam Detection System

SpamShield is a sophisticated email spam detection system that uses machine learning and rule-based approaches to identify unwanted emails. The system offers multiple detection modes tailored for different use cases, making it highly versatile for various email filtering needs.

## 🌟 Features

- **Multiple Detection Modes:**
  - General Mode: Standard spam detection for everyday use
  - Business Mode: Specialized for business communications
  - Commercial Mode: Focused on commercial email filtering
  - Daily Mode: Optimized for personal daily communications

- **Smart Detection System:**
  - Machine Learning based classification using Linear SVC
  - TF-IDF vectorization for text analysis
  - Custom black and white list management
  - Word weight-based scoring system

- **User-Friendly Interface:**
  - Clean and intuitive web interface
  - Real-time email scanning
  - Easy list management for black and white lists
  - Detailed feedback on detection results

## 🔧 Technical Architecture

### Backend (`/backend`)
- **`app.py`**: Flask application serving as the main backend server
- **`spamFilter.py`**: Core spam detection logic implementing ML algorithms
- **`cleanText.py`**: Text preprocessing and cleaning utilities
- **`datasets/`**: Contains training data and word lists
  - Black list and white list management
  - Mode-specific training datasets

### Frontend (`/frontend`)
- **`templates/`**: HTML templates for different views
- **`static/`**: Static assets (CSS, JavaScript, images)

## 🛠️ Technology Stack

- **Backend:**
  - Python 3.x
  - Flask (Web Framework)
  - scikit-learn (Machine Learning)
  - pandas & numpy (Data Processing)
  - openpyxl (Excel Data Handling)

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap (Responsive Design)

## 📋 Prerequisites

- Python 3.x
- pip (Python Package Manager)
- Required Python packages:
  ```
  flask
  scikit-learn
  pandas
  numpy
  openpyxl
  ```

## 🚀 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/canertunc/SpamShield.git
   cd SpamShield
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python backend/app.py
   ```

## 💡 Usage

1. **Select Detection Mode:**
   - Choose from General, Business, Commercial, or Daily mode based on your needs

2. **Scan Email:**
   - Paste the email content into the text area
   - Click "Scan" to analyze the content
   - Review the detailed detection results

3. **Manage Lists:**
   - Add words to the black list for automatic spam detection
   - Add words to the white list to prevent false positives
   - Access list management through the Lists menu

## 🔍 How It Works

1. **Text Preprocessing:**
   - Email content is cleaned and normalized
   - Text is vectorized using TF-IDF

2. **Detection Process:**
   - Checks against black and white lists
   - Applies machine learning model (Linear SVC)
   - Calculates word weights and scores
   - Provides detailed detection reasoning

3. **Mode-Specific Processing:**
   - Each mode uses specialized datasets and parameters
   - Custom weight adjustments per mode
   - Mode-specific word lists and thresholds

## ⚖️ Black List and White List System

One of SpamShield's most powerful features is its customizable black list and white list system.

### Black List:
- **Purpose**: Contains words that should definitely be marked as spam
- **How it Works**:
  - When a word is added to the black list, it is assigned a weight value of +100
  - If an email contains any word from the black list, it is automatically marked as spam
  - This allows users to define their own spam criteria
  - Example: Specific advertising terms or unwanted sender addresses

### White List:
- **Purpose**: Contains trusted words that should never be marked as spam
- **How it Works**:
  - When a word is added to the white list, it is assigned a weight value of -100
  - If an email is marked as spam and this is solely due to a word in the white list, the email will not be marked as spam
  - This helps prevent false positives
  - Example: Domain names of trusted business partners or important business terms

### List Management:
- Both lists can be dynamically updated
- Lists are stored in CSV format for easy management
- A word cannot be in both the black list and white list simultaneously
- When a word is added to one list, it is automatically removed from the other

### Recommended Usage:
1. **For Black List**:
   - Common words in recurring spam emails
   - Domain names of known spam senders
   - Unwanted product or service terms

2. **For White List**:
   - Domain names of business partners
   - Important customer names
   - Internal company terms
   - Frequently used business terminology

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

**Note:** Keep your black and white lists updated regularly for optimal detection results.


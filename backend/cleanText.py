from bs4 import BeautifulSoup  
import re  
import nltk  

def cleanString(myString):

    myString = myString.lower()

    myString = re.sub(r'(http|https)://[^\s]*', r' httpaddr ', myString)

    myString = re.sub(r'[^\s]+@[^\s]+[.][^\s]+', r' emailaddr ', myString)
    
    soup = BeautifulSoup(myString, 'html.parser')
    myString = soup.get_text()
    numberLink = len(soup.find_all('a'))
    numberImg = len(soup.find_all('img'))
    myString = myString + numberLink * " linktag " + numberImg * " imgtag "

    myString = re.sub(r'[0-9]+', r' number ', myString)

    myString = re.sub(r'[$]', r' dollar ', myString)
    myString = re.sub(r'[!]', r' exclammark ', myString)
    myString = re.sub(r'[?]', r' questmark ', myString)

    myString = re.sub(r'([^\w\s]+)|([_-]+)', r' ', myString)

    myString = re.sub(r'\n', r' newline ', myString)
    myString = re.sub(r'\n\n', r' blankline ', myString)
    myString = re.sub(r'\s+', r' ', myString)
    myString = myString.strip(' ')

    myStringWords = myString.split(' ')
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    stemWords = [stemmer.stem(word) for word in myStringWords]
    myString = ' '.join(stemWords)

    return myString

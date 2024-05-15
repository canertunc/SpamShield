from bs4 import BeautifulSoup  # BeautifulSoup kütüphanesini dahil ediyoruz
import re  # Regular expression kütüphanesini dahil ediyoruz
import nltk  # Natural Language Toolkit (NLP) kütüphanesini dahil ediyoruz

def cleanString(myString):
    """
    Metin temizleme işlemleri yapar.
    :param myString: Temizlenecek metin
    :return: Temizlenmiş metin
    """

    # Metni küçük harfe dönüştürme
    myString = myString.lower()

    # URL'leri 'httpaddr' olarak dönüştürme
    myString = re.sub(r'(http|https)://[^\s]*', r' httpaddr ', myString)

    # E-posta adreslerini 'emailaddr' olarak dönüştürme
    myString = re.sub(r'[^\s]+@[^\s]+[.][^\s]+', r' emailaddr ', myString)
    
    # Tüm bağlantıları 'linktag' olarak dönüştürme
    # Tüm img etiketlerini 'imgtag' olarak dönüştürme
    soup = BeautifulSoup(myString, 'html.parser')
    myString = soup.get_text()
    numberLink = len(soup.find_all('a'))
    numberImg = len(soup.find_all('img'))
    myString = myString + numberLink * " linktag " + numberImg * " imgtag "

    # Sayıları 'number' olarak dönüştürme
    myString = re.sub(r'[0-9]+', r' number ', myString)

    # $, ! ve ? işaretlerini uygun kelimelere dönüştürme
    myString = re.sub(r'[$]', r' dollar ', myString)
    myString = re.sub(r'[!]', r' exclammark ', myString)
    myString = re.sub(r'[?]', r' questmark ', myString)

    # Diğer noktalama işaretlerini boşluk olarak dönüştürme
    myString = re.sub(r'([^\w\s]+)|([_-]+)', r' ', myString)

    # Yeni satırları ve boş satırları özel dizeye dönüştürme ve ekstra boşlukları tek boşluk haline getirme
    myString = re.sub(r'\n', r' newline ', myString)
    myString = re.sub(r'\n\n', r' blankline ', myString)
    myString = re.sub(r'\s+', r' ', myString)
    myString = myString.strip(' ')

    # Kelime köklerini bulma
    myStringWords = myString.split(' ')
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    stemWords = [stemmer.stem(word) for word in myStringWords]
    myString = ' '.join(stemWords)

    return myString

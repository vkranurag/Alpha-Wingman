from flask import Blueprint, render_template, request, redirect, flash
import os
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/summary')
def summary():
    return render_template("index.html")

@views.route('/stt')
def speechtotext():
    return render_template("speech-to-text.html")

@views.route('/grammarcheck')
def grammarcheck():
    return render_template("grammarcheck.html")

@views.route("/grammarcheck", methods=['GET', 'POST'])
def streambyte():
    # your file processing code is here...
    text = request.form['text']
    # your file processing code is here...

    return render_template('grammarcheck.html', result = grammar(text))


@views.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        link = request.form["link"]
        dictStr = str(request.form.values)

        length = ""
        
        if "Short Summary" in dictStr:
            length = "short"
        else:
            length = "long"
        created_summary = get_summary(link,length)
    return render_template("results.html", summary = created_summary)

def get_summary(link, length):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    nltk.download('stopwords','nltk_data')
    nltk.download('punkt','nltk_data')
    import bs4 as bs
    import urllib.request
    import re
    from scipy import stats

    scraped_data = urllib.request.urlopen(link)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'html.parser')

    paragraphs = parsed_article.find_all('p')

    text = ""

    for p in paragraphs:
        text += p.text
   
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()
   
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else: 
                    sentenceValue[sentence] = freq 
    
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    
    average = int(sumValues / len(sentenceValue))

    s = []
    for i, j in sentenceValue.items():
        s.append(j)

    u1, u2 = stats.describe(s).minmax
    u3, u4 = u1/stats.describe(s).mean, u2/stats.describe(s).mean

    l1 = (u4 - u3) - 0.1
    l2 = (u4 - u3) - 0.2

    if length == 'short':
      while True:
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (l1 * average)):
                summary += " " + sentence

        word_list= summary.split( )

        for word in word_list:
            if ']' in word or '[' in word:
                word_list.remove(word)

        final_summary = ''

        for word in word_list:
            final_summary+= word + " "

        th = len(final_summary.split())/len(text.split())
        if (th >= 0.15) and (th <= 0.25):
            break
        elif (th >= 0.01) and (th <= 0.15):
            l1 -= 0.02
        elif (th >= 0.25) and (th <= 0.35):
            l1 += 0.02
        elif (th >= 0.35) and (th <= 0.5):
            l1 += 0.05
        elif (th >= 0.5) and (th <= 0.7):
            l1 += 0.1
        elif (th >= 0.7) and (th <= 1):
            l1 += 0.1
      return final_summary
    
    if length == 'long':
      while True:
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (l2 * average)):
                summary += " " + sentence

        word_list= summary.split( )

        for word in word_list:
            if ']' in word or '[' in word:
                word_list.remove(word)

        final_summary = ''

        for word in word_list:
            final_summary+= word + " "
        th = len(final_summary.split())/len(text.split())
        if (th >= 0.25) and (th <= 0.35):
            break
        elif (th >= 0.01) and (th <= 0.1):
            l2 -= 0.1
        elif (th >= 0.1) and (th <= 0.25):
            l2 -= 0.05
        elif (th >= 0.35) and (th <= 0.5):
            l2 += 0.05
        elif (th >= 0.5) and (th <= 0.7):
            l2 += 0.1
        elif (th >= 0.7) and (th <= 1):
            l2 += 0.1
      return final_summary

def grammar(text):
    from gingerit.gingerit import GingerIt

    parser = GingerIt()
    return "After correction :"+parser.parse(text)['result']
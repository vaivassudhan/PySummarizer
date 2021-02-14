import os
import speech_recognition as sr
from multi_rake import Rake
import nltk 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

def _create_frequency_table(text_string) -> dict:

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable
def _score_sentences(sentences, freqTable) -> dict:
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] // word_count_in_sentence

    return sentenceValue
def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return average
def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary
# com1="ffmpeg -i demo.mp4 demo.mp3"
# com2= "ffmpeg -i demo.mp3 demo.wav"
# os.system(com1)
# os.system(com2)
# r = sr.Recognizer()
# audio = sr.AudioFile('demo.wav')
# with audio as source:
#     audio = r.record(source,duration=100000)
# text=(r.recognize_google(audio))

print()
print()
# text="""
# There are times when the night sky glows with bands of color. The bands may begin as cloud shapes and then spread into a great arc across the entire sky.
# They may fall in folds like a curtain drawn across the heavens. The lights usually grow brighter, then suddenly dim. During this time the sky glows with pale yellow, pink, green, violet, blue, and red. 
# These lights are called the Aurora Borealis. Some people call them the Northern Lights. Scientists have been watching them for hundreds of years. They are not quite sure what causes them. In ancient times
# people were afraid of the Lights. They imagined that they saw fiery dragons in the sky. Some even concluded that the heavens were on fire.
# """
text="""
Allahrakha Rahman (About this soundpronunciation; born A. S. Dileep Kumar on 6 January 1967), known professionally as A. R. Rahman, is an Indian composer, musician, singer, and music producer who works predominantly in Tamil and Hindi films. 
In 2010, the Indian government awarded him the Padma Bhushan, the nation's third-highest civilian award.Among Rahman's awards are six National Film Awards, two Academy Awards, two Grammy Awards, a BAFTA Award, a Golden Globe Award, fifteen Filmfare Awards and seventeen Filmfare Awards South.
Rahman initially composed scores for different documentaries and jingles for advertisements and Indian television channels. With his in-house studio Panchathan Record Inn, Rahman's film-scoring career began during the early 1990s with the Tamil film Roja.
Following that, he went on to score several songs for Tamil language films, including Ratnam's politically charged Bombay, the urban Kadhalan, Thiruda Thiruda, and S. Shankar's debut film Gentleman. 
Rahman's score for his first Hollywood film, the comedy Couples Retreat (2009), won the BMI Award for Best Score. His music for Slumdog Millionaire (2008) earned him Best Original Score and Best Original Song at the 81st Academy Awards. 
He was also awarded Best Compilation Soundtrack Album and Best Song Written for Visual Media at the 2010 Grammy Awards. He is nicknamed "Isai Puyal" (musical storm) and "Mozart of Madras".
Rahman has also become a humanitarian and philanthropist, donating and raising money for a number of causes and charities. In 2006, he was honoured by Stanford University for his contributions to global music.
In 2008, he received Lifetime Achievement Award from the Rotary Club of Madras.[6] In 2009, he was included on the Time list of the world's 100 most influential people.In 2013, he introduced 7.1 surround sound technology to South Indian films.
In 2014, he was awarded an honorary doctorate from Berklee College of Music. He has also received honorary doctorate from Aligarh Muslim University.
In 2017, he made his debut as a director and writer for the film Le Musk."""
freq_table = _create_frequency_table(text)
print("FREQ TABLE_____")
print(freq_table)

sentences = sent_tokenize(text)
print("SENTENCES_____")
print(sentences)
# 3 Important Algorithm: score the sentences
sentence_scores = _score_sentences(sentences, freq_table)

# 4 Find the threshold
threshold = _find_average_score(sentence_scores)

# 5 Important Algorithm: Generate the summary
summary = _generate_summary(sentences, sentence_scores, 1 * threshold)

print("SUMMARY____")
print(summary)
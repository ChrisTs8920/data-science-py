import string

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk.book import *
from nltk.tokenize import *


def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(count, total):
    return 100 * count / total


def clear_punc_stopwords(text, language):
    stopwords = nltk.corpus.stopwords.words(language)
    cleaned_tokens = []
    for token in text:
        if token not in string.punctuation and token not in stopwords:
            cleaned_tokens.append(token)
    return cleaned_tokens


def main():
    print("\nTEXT6:")
    # lexical richness
    r = lexical_diversity(text6)
    print("\nLexical richness of text6:", round(r * 100, 2), "%")  # in percentage

    # sum of "LAUNCELOT"
    c = text6.count("LAUNCELOT")
    print("LAUNCELOT shows", c, "times.")

    # percentage of text is taken up by "LAUNCELOT"
    p = percentage(text6.count("LAUNCELOT"), len(text6))
    print("Percentage of LAUNCELOT:", round(p, 2), "%")

    t6 = ["not", "Python", "Holy"]

    for i in t6:
        p = percentage(text6.count(i), len(text6))
        print("Percentage of", i, ":", round(p, 2), "%")

    print("\nTEXT5:")
    # lexical richness
    r = lexical_diversity(text5)
    print("\nLexical richness of text5:", round(r * 100, 2), "%")  # in percentage

    # sum of "omg"
    c = text5.count("omg")
    print("omg shows", c, "times.")
    # percentage of text is taken up by "omg"
    p = percentage(text5.count("omg"), len(text5))
    print("Percentage of 'omg':", round(p, 2), "%")

    # sum of "OMG"
    c = text5.count("OMG")
    print("OMG shows", c, "times.")
    # percentage of text is taken up by "OMG"
    p = percentage(text5.count("OMG"), len(text5))
    print("Percentage of 'OMG':", round(p, 2), "%")

    # sum of "lol"
    c = text5.count("lol")
    print("lol shows", c, "times.")
    # percentage of text is taken up by "lol"
    p = percentage(text5.count("lol"), len(text5))
    print("Percentage of 'lol':", round(p, 2), "%")

    t5 = ["Corpus", "before", "and"]

    for i in t5:
        p = percentage(text5.count(i), len(text5))
        print("Percentage of", i, ":", round(p, 2), "%")

    fdist1 = FreqDist(text1)
    fdist1.most_common(50)
    plt.figure(figsize=(15, 9))
    fdist1.plot(50, title="50 most common words for Moby Dick (text1)")

    fdist1 = FreqDist(text6)
    fdist1.most_common(50)
    plt.figure(figsize=(15, 9))
    fdist1.plot(
        50, title="50 most common words for Monty Python and the Holy Grail (text6)"
    )

    tokens1 = text2[0:200]  # first 200 tokens from book 2
    porter = nltk.PorterStemmer()
    st = [porter.stem(t) for t in tokens1]

    nltk.download("wordnet")
    wnl = nltk.WordNetLemmatizer()
    lem = [wnl.lemmatize(t) for t in tokens1]

    # Stemming vs Lemmatize
    print("\nSTEMMING VS LEMMATIZATION")

    print("\nStemmed first 200 tokens from text2:\n", st)
    print("\nLemmatized first 200 tokens from text2:\n", lem)

    # greek text used to compare stemming and lemmatization
    raw = """Ερώτηση 5: Κάντε πειράματα με δικές σας προτάσεις-κείμενα. Δοκιμάστε και ελληνικό κείμενο.
            Εμφανίστε τα αποτελέσματά σας και γράψτε τα σχόλιά σας με κριτική άποψη κάνοντας σύγκριση των
            δύο παραπάνω τεχνικών καθώς και τη σύγκριση με την απλή κανονικοποίηση, παρουσιάζοντας τα
            θετικά και τα αρνητικά κάθε μίας."""
    my_text = word_tokenize(raw)

    porter = nltk.PorterStemmer()
    st = [porter.stem(t) for t in my_text]
    wnl = nltk.WordNetLemmatizer()
    lem = [wnl.lemmatize(t) for t in my_text]

    print("\nStem for my_text variable:\n", st)
    print("\nLemmatize for my_text variable:\n", lem)

    joined = " ".join(tokens1)  # convert from tokens to raw string

    split_text2 = joined.split()
    tokenized_text2 = nltk.word_tokenize(joined)

    # Stemming vs Lemmatize
    print("\nSPLIT VS TOKENIZER")

    print("\nUsing Split:\n", split_text2)
    print("\nUsing Tokenizer:\n", tokenized_text2)

    # greek text used to compare str.split() and nltk.word_tokenize()
    raw = """Ερώτηση 6: Κάντε πειράματα με δικές σας προτάσεις-κείμενα καθώς και με τις πρώτες 200 λέξεις του
            βιβλίου «Sense and Sensibility». Δοκιμάστε και ελληνικό κείμενο. Εμφανίστε τα αποτελέσματά σας
            και γράψτε τα σχόλιά σας με κριτική άποψη κάνοντας σύγκριση των δύο παραπάνω τεχνικών,
            παρουσιάζοντας τα θετικά και τα αρνητικά κάθε μίας."""
    my_text_split = raw.split()
    my_text_tokenized = nltk.word_tokenize(raw)

    print("\nUsing Split for my_text:\n", my_text_split)
    print("\nUsing Tokenizer for my_text:\n", my_text_tokenized)

    print("\nPunctuations:", string.punctuation)  # prints punctuations

    # see stopwords
    # nltk.download("stopwords")
    # stopwords_eng = nltk.corpus.stopwords.words("english")
    # stopwords_gr = nltk.corpus.stopwords.words("greek")

    # count stopwords
    # count_eng = len(stopwords_eng)
    # count_gr = len(stopwords_gr)

    # print("\nEnglish stopwords count:", count_eng)
    # print("English stopwords:\n", stopwords_eng)
    # print("\nGreek stopwords count:", count_gr)
    # print("Greek stopwords:\n", stopwords_gr)

    cleaned_tokenized_text2 = clear_punc_stopwords(tokenized_text2, "english")

    print("\nClean English text2:\n", cleaned_tokenized_text2)

    # greek text used to compare vs 'cleaned' text.
    raw = """Ερώτηση 8: Καλέστε την συνάρτηση που φτιάξατε για να καθαρίσετε το κείμενο με τις πρώτες 200
            λέξεις του βιβλίου «Sense and Sensibility». Κάντε πειράματα με δικές σας προτάσεις-κείμενα.
            Δοκιμάστε και ελληνικό κείμενο. Εμφανίστε τα αποτελέσματά σας και γράψτε τα σχόλιά σας με
            κριτική άποψη για τα συμπεράσματα που βγάζετε από τα πειράματά σας."""
    my_text_tokenized = nltk.word_tokenize(raw)

    cleaned = clear_punc_stopwords(my_text_tokenized, "greek")
    print("\nClean Greek text:\n", cleaned)

    # show initial text2
    fdist1 = FreqDist(tokens1)
    fdist1.most_common(50)
    plt.figure(figsize=(15, 9))
    fdist1.plot(50, title="50 most common words for Sense and Sensibility (text2)")

    # show clean text2
    tokenized_normalized_text2 = [x.lower() for x in cleaned_tokenized_text2]
    cleaned_tokenized_normalized_text2 = clear_punc_stopwords(
        tokenized_normalized_text2, "english"
    )
    fdist1 = FreqDist(cleaned_tokenized_normalized_text2)
    fdist1.most_common(50)
    plt.figure(figsize=(15, 9))
    fdist1.plot(
        50, title="50 most common words for 'clean' Sense and Sensibility (text2)"
    )  # clean = removed stopwords, normalized and tokenized.


if __name__ == "__main__":
    main()
    plt.show()

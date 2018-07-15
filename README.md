# natural-language-processing


## Terms related :

### Corpus 
Body of text, singular. Corpora is the plural of this.
### Lexicon 
Words and their meanings.
### Token 
Each “entity” that is a part of whatever was split up based on rules. For examples, each word is a token when a sentence is “tokenized” into words. Each sentence can also be a token, if you tokenized the sentences out of a paragraph.
### StopWords
Stop Words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.
### Stemming
Stemming is the process of producing morphological variants of a root/base word. Stemming programs are commonly referred to as stemming algorithms or stemmers. 

------
# METHODS :

## 1.Tokenization

#### word_tokenize()
A sentence or data can be split into words using this method.

#### sent_tokenize()
A paragraph or a piece of text can be broken down into sentences.  
  
##### Refer to tokenize.py

---

## 2.Stopwords
In natural language processing, useless words (data), are referred to as stop words. We can remove them easily, by storing a list of words that you consider to be stop words.  

--
#### stopwords.words('english')  
Following are some stopwords:  
  
<img width="480" alt="aa" src="https://user-images.githubusercontent.com/39124232/42733529-4a40d17c-8850-11e8-980e-f7e0121a435c.PNG">
  
##### Refer to stopwords.py

---

## 3.Stemming
A stemming algorithm reduces the words “chocolates”, “chocolatey”, “choco” to the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce to the stem “retrieve”.

#### Applications of stemming are:

Stemming is used in information retrieval systems like search engines.  
It is used to determine domain vocabularies in domain analysis.  

###### Google search adopted word stemming in 2003. Previously a search for “cat” would not have returned “catty” or “cats”.  

#### Some Stemming algorithms are:
### Potter’s Stemmer algorithm
It is one of the most popular stemming methods proposed in 1980. It is based on the idea that the suffixes in the English language are made up of a combination of smaller and simpler suffixes.  
Example: EED -> EE means “if the word has at least one vowel and consonant plus EED ending, change the ending to EE” as ‘agreed’ becomes ‘agree’.  
Advantage: It produces the best output as compared to other stemmers and it has less error rate.  
Limitation:  Morphological variants produced are not always real words.    
### Lovins Stemmer
It is proposed by Lovins in 1968, that removes the longest suffix from a word then word is recoded to convert this stem into valid words.  
Example: sitting -> sitt -> sit  
Advantage: It is fast and handles irregular plurals like 'teeth' and 'tooth' etc.  
Limitation: It is time consuming and frequently fails to form words from stem.  
### Dawson Stemmer
It is extension of Lovins stemmer in which suffixes are stored in the reversed order indexed by their length and last letter.  
Advantage: It is fast in execution and covers more suffices.  
Limitation: It is very complex to implement.  
### Krovetz Stemmer
It was proposed in 1993 by Robert Krovetz. Following are the steps:  
1) Convert the plural form of a word to its singular form.  
2) Convert the past tense of a word to its present tense and remove the suffix ‘ing’.  
Example: ‘children’ -> ‘child’  
Advantage: It is light in nature and can be used as pre-stemmer for other stemmers.  
Limitation: It is inefficient in case of large documents.  
### Xerox Stemmer
Advantage: It works well in case of large documents and stems produced are valid.  
Limitation: It is language dependent and mainly implemented on english and over stemming may occur.  
### N-Gram Stemmer
An n-gram is a set of n consecutive characters extracted from a word in which similar words will have a high proportion of n-grams in common.  
Example: ‘INTRODUCTIONS’ for n=2 becomes : *I, IN, NT, TR, RO, OD, DU, UC, CT, TI, IO, ON, NS, S*  
Advantage: It is based on string comparisons and it is language dependent.   
Limitation: It requires space to create and index the n-grams and it is not time efficient.  
##### Refer stemming.py
---

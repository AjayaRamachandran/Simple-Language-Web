# Simple Language Web

## Overview
Simple Language Web is an extremely simple language model written in Python that uses a web of word associations as a method of generating simple sentences.


## Breakdown
The SLW model uses a weighted language network. It uses hundreds of thousands of word associations to connect words in sequence, and can be used to generate simple sentences. As this model is incredibly simple, these sentences may have the tendency to not make sense.

SLW works by analyzing large sets of text, and creating a library of tagged words. Each word will have a numerical identifier, which allows different relations between words to be notated in one single file. With each word will be a weighted sub-list of words (not the words themselves, but their identifiers) that could follow the word in question. When a pair of words is encountered by the text reader, it adds a point to the weight of the second word in the sub-list of the first word. As the analysis continues, words that follow the first word more often will garner higher weights. There will also be a special weighted sub-list for words that start sentences, and special sub-list for words that end sentences.

When asked to generate a string of words, SLW will first pick a word to start the sentence off with, which chosen at random from the weighted sub-list of sentence starters. Once this is done, SLW simply follows the web of words, choosing the next word at random (it is a weighted randomness) from the possible options in the web. As SLW makes its way through a sentence, it may come across a word that is also a member of a sentence-ending words list. If so, it randomly chooses between continuing the sentence or ending it, and if ending it places a period and the sentence finishes.

From this analysis, it is clear that only on rare occasion will SLW generate anything that is remotely intelligent. However, this technology, if trained on a large database of text messages, for example, could be a useful tool for predictive typing.

## API
Once SLW is complete, there will be documentation on the use of different functions and methods here. For now, enjoy this smiley face. :)

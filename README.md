# Simple Language Web

## Overview
Simple Language Web is an extremely simple language model written in Python that uses a web of word associations as a method of generating simple sentences.

## Breakdown
The SLW model is essentially a weighted language network. It uses hundreds of thousands of word associations to connect words in sequence, and can be used to generate simple sentences. As this model is incredibly simple, these sentences may have the tendency to not make sense.

SLW works by analyzing large sets of text, and creating a library of tagged words. Each word will have a numerical identifier, which allows different relations between words to be notated in one single file. With each word will be a weighted sub-list of words (not the words themselves, but their identifiers) that could follow the word in question. When a pair of words is encountered by the text reader, it adds a point to the weight of the second word in the sub-list of the first word. As the analysis continues, words that follow the first word more often will garner higher weights. There will also be a special weighted sub-list for words that start sentences, and special sub-list for words that end sentences.

When asked to generate a string of words, SLW will first pick a word to start the sentence off with, which chosen at random from the weighted sub-list of sentence starters. Once this is done, SLW simply follows the web of words, choosing the next word at random (it is a weighted randomness) from the possible options in the web. As SLW makes its way through a sentence, it may come across a word that is also a member of a sentence-ending words list. If so, it randomly chooses between continuing the sentence or ending it, and if ending it places a period and the sentence finishes.

From this analysis, it is clear that only on rare occasion will SLW generate anything that is remotely intelligent. However, this technology, if trained on a large database of text, could have some useful applications.

## Applications
The SLW model, once trained on large amounts of data, will essentially have a large text file that consists of thousands of words, each with a sublist of perhaps tens of possible following words. This file will be very big, and there are issues with using such a file, but leaving logistics aside for a moment, let's explore some possible applications for such a model.

### Generating Sentences
SLW would essentially be able to generate (perhaps nonsensical) fluent sentences on command. These sentences would have little more than basic word-to-word connection, and on a scale of just a few words or more will not make sense. However, this on its own still has its uses. In a typing test program, for example, SLW could be used to create basic material to practice typing on. Most applications of this sentence-generating ability are best used in tandem with other things (see below: collaborative applications)

### Predicting Upcoming Words
SLW would also have the ability to predict future words based on the last typed word in a sentence. If trained on a dataset of text messages, for example, SLW could be very useful for predictive typing, and would have the ability to look 1, 2, or even 3 words ahead in a sentence.

## Collaborative Applications
Working with other models and systems, SLW may be able to accomplish far more. Below are some possible applications of SLW when working with other systems.

### Grammar Checking or Suggesting
SLW, if trained on grammatically correct data, would have nearly perfect word-to-word knowledge on grammar patterns. With this ability, SLW could analyze a word in a given bit of typed text, and see if it is not the highest-weighted option (or maybe not one of the options at all) for the word that came before. If so, SLW might be able to make a suggestion for swapping out said word for one that fits "better" in that spot. This, however, would need to work together with a model that could identify different parts of speech, or otherwise SLW might make replacement suggestions for things that should not be replaced (this is why it is a collaborative application)

### Paraphrasing Sentences
SLW would have knowledge on word fluency - if combined with a model that could discern parts of speech (like the above example), it might be able to take a user-inputted sentence, analyze all the key aspects, and reconstruct a new sentence that keeps all those aspects but introduces a new tone or structure. This application is however the most speculative, as to accomplish this level of fine control would require a "smarter" algorithm - perhaps one that uses machine learning.

## API
Once SLW is complete, there will be documentation on the use of different functions and methods here, so you can use it as a module in your own projects. For now, enjoy this smiley face. :)

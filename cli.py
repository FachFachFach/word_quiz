# this is a cli version of the word_quiz app
"""
to do list:
	make sure the code works
    split the code into functions accordingly
""" 




# from googletrans import Translator

# words = ['car', 'cat', 'dog']
# destination = input("[?] destinatin language : ").strip().casefold()

# if destination in dict(map(reversed, googletrans.LANGUAGES.items())).keys(): ## checks all the suported language
# 	destination = dict(map(reversed, googletrans.LANGUAGES.items()))['Hebrew']  ##gets the languagae code

	
# for w in words:
# 	try:
# 		print(translator.translate(w, dest=destination).text)
# 	except Exception as ex:
# 		print(ex)




########################
#information about a car deck would include - word in language you would like to practice and a few (probably 4) words in the desired native language, and only one of these words would be - 
#the correct translation to the copied word mentioned above, the 3 other words would probably be other translations of words you've copied or just random words out of a word bank.
########################
#card_decks = {word_to_translate : [correct_translation, false_translation1, false_translation2, false_translation3, false_translation4], ... }

#########################################################################################################################################################3333
# word_quiz cli app version

from googletrans import Translator
from random import shuffle


# create translator object
translator = Translator()

word_bank = ['dog', 'cat', 'horse', 'magic', 'house', 'car', 'possible', 'phone', 'bottle']
# shuffle the word bank
# select 3 words from it
new_word_bank = shuffle(word_bank)
word1, word2, word3 = new_word_bank[0], new_word_bank[1], new_word_bank[2]

word_to_translate = '' # ex - dog, cat, car. in practice we wont need to use this as it would be grabbed from the clipboard

words = shuffle([word1, word2, word3, word_to_tranlate])
# src language detection
src_language = translator.detect(word_to_translate)


# dest language selection
dest_language = input('destination language: ').strip().casefold() # english, hebrew, hindu, german, japanese...

if dest_language in dict(map(reversed, googletrans.LANGUAGES.items())).keys(): # checks all the supported language
	dest_code = dict(map(reversed, googletrans.LANGUAGES.items()))['Hebrew']  # gets the language code

# pretty sure this whole thing needs to go into the if statement

#### error handling needs to be added here
translated_word = translator.translate(word_to_translate, src=src_language, dest=dest_language).text 
####

word_index = 1
translated_words = {}
for w in words:
	try:
    	translated_word = translator.translate(w, src=src_language, dest=dest_code).text
        translated_words[word_index] = translated_word
		print(word_index, translated_word)
        word_index += 1
	except Exception as ex:	
		print(ex)


print('select correct translation (index)- ')
print(word_to_translate, '\n', translated_words)

chosen_index = input('chosen index (integer): ')
chosen_word = translated_words.get(chosen_index)
# evaluate chosen word against the translation of word_to_translate
if chosen_word == translated_word:
	print(True)
else:
	print(False)




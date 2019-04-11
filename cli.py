# this is a cli version of the word_quiz app
"""
to do list:
	1. add a User class - contains user prefrences and info (dest_language, custom word_bank, save/update user information)
	2. save user information in a file using pickle
	3. move user dependant functionality from the Quiz class to the User class
	
""" 
#from googletrans import Translator
import googletrans
from random import shuffle
from bidi import algorithm

# create translator object
translator = googletrans.Translator()

class Quiz:
	def __init__(self, name, word_to_translate):
		self.name = name
		self.dest_language_code = self.set_dest_language()
		self.word_to_translate = word_to_translate
		
		# keep the word_bank static for now, the intention is for it to be dynamic -
		# dependent upon 
		#example of a word_bank
		self.word_bank = [
		'dog', 'cat', 'horse', 'magic', 'house'
		, 'car', 'possible', 'phone', 'bottle']
	
	def set_dest_language(self):
		"""
		1. print a list of avaliable languages to translate to
		2. let the user choose a preferred destination languages of of the 'avaliable languages list
		3. set the destination language to the chosen language by the user
		else - raise an error
		"""
		#1.
		print('list of avaliable languages: \n')
		languages_dict = dict(map(reversed, googletrans.LANGUAGES.items()))
		for language in languages_dict.keys():
			print(language)
		
		dest_language = input('choose a language to translate to: ')
		if dest_language in languages_dict.keys():
			dest_language_code = dict(map(reversed, googletrans.LANGUAGES.items()))[dest_language]
			
			return dest_language_code
		else:
			raise Exception('desired language not found')

	def generate_quiz(self):
		shuffle(self.word_bank)
		words = self.word_bank[:3]; words.append(self.word_to_translate)
		#shuffle(words)
		# src language code detection
		src_language = translator.detect(self.word_to_translate).lang
		print(src_language)

		try:
			translations = [algorithm.get_display(i.text) for i in translator.translate(words, src=src_language, dest=self.dest_language_code)]
		except Exception as e:
			print(e)
		else:
			self.translated_word = translations[-1]
			shuffle(translations)
			return translations

	def user_prompt(self, translations):
		# user prompt:
		print('select correct translation (index) - \n word: {}'.format(self.word_to_translate))
		
		for i, j in enumerate(translations):
			print('index: {}, word: {}'.format(i,j))
		
		chosen_index = int(input('chosen index (integer): '))
		chosen_word = translations[chosen_index]
		# evaluate chosen word against the translation of word_to_translate
		if chosen_word == self.translated_word:
			return True
		else:
			return False


""""
# dest language selection
dest_language = input('destination language: ').strip().casefold() # english, hebrew, hindu, german, japanese...

if dest_language in dict(map(reversed, googletrans.LANGUAGES.items())).keys(): # checks all the supported language
	dest_code = dict(map(reversed, googletrans.LANGUAGES.items()))['Hebrew']  # gets the language code
else:
	print('such a language does not exist in the languages dictionary')
# pretty sure this whole thing needs to go into the if statement
"""
#### error handling needs to be added here

####


def main():
	name = 'gal'
	word_to_translate = 'hello'  # ex - dog, cat, car. in practice we wont need to use this as it would be grabbed from the clipboard

	quiz = Quiz(name, word_to_translate)
	translated_words = quiz.generate_quiz()
	result = quiz.user_prompt(translated_words)
	print('result: ', result)
if __name__ == '__main__':
	main()

"""
1.  we will take input from user (afterwards it will be taken from clipboard)
2.  make a list of 4 words ( 3 random words and the input word )
3.  translate the list into the destination language (given by the user at run time)
4.  ask the user to tell which is the correct translation of the input word
5.  if selected answer is correct then end it...else continue it with a "wrong answer" prompt.
"""

from googletrans import Translator, LANGUAGES
from random import shuffle


def main():
    word_to_translate =  input("[?]word to translate: ")  # 1
    translator = Translator()
    # returns language tupple... use ".lang" for gettign actual language
    src_lang = translator.detect(word_to_translate)
    print("[+] Input Language detected : ",src_lang.lang)

    word_bank = ['dog', 'cat', 'horse', 'magic',
        'house', 'car', 'possible', 'phone', 'bottle']
    shuffle(word_bank)
    words = [*word_bank[:3], word_to_translate]  # 2
    shuffle(words)

    # english, hebrew, hindu, german, japanese...
    dest_lang = input('[?]destination language: ').strip().casefold()
    dest_code = ''
       # checks all the supported language
    if dest_lang in dict(map(reversed, LANGUAGES.items())).keys():
        dest_code = dict(map(reversed, LANGUAGES.items()))[dest_lang]  # gets the language code

    print("[+] Destination language : ",dest_code)
    print("Choose one\n")

    for i, w in zip(range(len(words)),translator.translate(words,src=src_lang.lang, dest=dest_code)): # 3
        print(i+1, '.  ',w.text)


    option = int(input("[?] Option: ")) # 4

    if words[option-1] == word_to_translate: # 5
        print("Correct Answer!!\n\n")
    else:
        print("Wrong Answer..")

    print(word_to_translate,translator.translate(word_to_translate,src=src_lang.lang, dest=dest_lang).text, sep='('+src_lang.lang+') => ('+dest_code+')')


# # # # # # # # DRIVER CODE # # # # # # # # # #
try:
    main()
except Exception as ex:
    print(ex.args[0])

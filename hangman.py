import random
import string

#just visual json dictonary
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

words = ["Partička","krokodýl", "smaženice", "houby", "kolo","anděl","kočka","auto","ekonomie","politika","písek","voda","země","počítač","obrazovka","myš","klávesnice","USB","Github","miska","vidlička","lednička","nůž","matematika","příklad"]
#falwnodidkxom
def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
#alfniw
#dlfpwondifksomcniks
#game loop
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 

    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print('Tvůj počet životů: ', lives)
        print("Použitá písmena: ",' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Slovo: ', ' '.join(word_list))

        user_letter = input('Hadané písmeno: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
#dalfniwkd
            else:
                lives = lives - 1 
                print('\nPísmeno,', user_letter, 'není ve slově.')

        elif user_letter in used_letters:
            print('\nTohle písmeno už si zkoušel.')

        else:
            print('\nTohle není písmeno.')
            
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Prohrál jsi. Slovo, které jsi měl/a uhodnout: ', word)
    else:
        print('SUPER! Uhodl/a jsi to - ', word, '!!')

#falwnoid
#afwopqnodfnick
#falwniqkdmc
if __name__ == '__main__':
    hangman()

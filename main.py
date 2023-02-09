def prGreen(skk): print("\033[92m {}\033[00m".format(skk), end = " ")
 
def prYellow(skk): print("\033[93m {}\033[00m".format(skk), end = " ")

word_list = []
word = "happy"

counter = 6
print("_ _ _ _ _")

while counter > 0:

    player = input("Guess a word: ")

    if len(player) != 5:
        print("Please enter a 5 letter word")
    elif player == word:
        print("You win !")
        break
    else:
        counter -= 1
        for pChar, wChar in zip(player, word):
            if pChar == wChar: #char in word and word.index(char, ) == player.index(char):
                prGreen(pChar)
            elif pChar in word:
                prYellow(pChar)
            else:
                print(pChar, end = " ")
        print("")
        print("Number of guesses left:", counter)

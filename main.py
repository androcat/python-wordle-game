def prGreen(skk): print("\033[92m {}\033[00m".format(skk), end = " ")
 
def prYellow(skk): print("\033[93m {}\033[00m".format(skk), end = " ")

word_list = []
word = "happy"

counter = 6
print("_ _ _ _ _")

while counter > 0:
    counter -= 1

    player = input("Guess a word: ")

    if player == word:
        "You win !"
        break
    else:
        for char in word:
            if char in player and word.index(char) == player.index(char):
                prGreen(char)
            elif char in player:
                prYellow(char)
            else:
                print("_", end = " ")

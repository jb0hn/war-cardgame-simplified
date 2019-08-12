# Welcome to the simplified version of the popular card game - War!

Yes, I made this extremely simple game even simpler! Now Your only task is just to press the Enter and watch results! Forget about tedious shuffling, dealing and exchanging cards!

The game is designed for two person but it doesn't matter, if you don't have another human player. Due to the simplicity of the production, the game will be looking exactly the same, it doesn't matter who you're playing against!

**To run online**

Just click in the link:

https://repl.it/@jb0hn/war-cardgame-simplified 

and after being redirected to the Repl.it website, make sure that "main.py" file is open and then click green button "Run" in the top bar of the page. 




**To run on GNU/Linux, open the Terminal and paste:**

    cd /path/to/the/game/folder

    python3 game.py


**To run on Windows, open Command Prompt (cmd.exe) and paste:**

    cd /path/to/the/game/folder

    python game.py


The game was tested on GNU/Linux (Ubuntu 16.04.2 with Python 3.5.2), Windows (Windows 10 with Python 3.6.4) and Repl.it (August 2019).


## Instruction

#### Example nr 1:

          Jan[8]: 4♥ (4)
          Paweł[9]: J♣ (11)

Everything works as follow. Beginning on the left, you will see a player name, moving right you will see his/her/its total score in this game, given in square brackets. The player who will have greater total score after the deck is empty - wins! Next, there's a colon but it's completely negligible and appears there only because of aesthetic reasons. Going further to the right you will notice a number or a letter - that's a rank of your card! It's follow by it's suit, in a form of a nice Unicode character. The last value, which is contained in round brackets is "power" of your actual hand. The player with greater score in this particular parenthesis wins the deal and gains **1 point**!

#### Example nr 2:

          Jan[12]: 10♣ (10)
          Paweł[11]: 10♥ (10)

          WAR OUTBREAK!!!

          Jan[12]: 10♣ 🂠
          Paweł[11]: 10♥ 🂠
          Jan[12]: 10♣ 🂠 8♣
          Paweł[11]: 10♥ 🂠 9♥
          Jan[12]: 8♣ (8)
          Paweł[11]: 9♥ (9)

Sometimes it could happen that you and your opponent will have the same "power" in a deal. It'll lead to the massive conflict called **WAR**. But don't worry, it's incredibly simple game and everything will happens as follow. Both of you will throw an extra card in but it will remain covered! Then, you will throw one more card in but this time, the card will be graded by my extremely sophisticated algorithm, which will result in displaying a new "power". And as in an ordinary deal, the player with higher power wins, gaining this time whole **3 points**!

That's it. Have a nice game and don't overwork your Enter button!

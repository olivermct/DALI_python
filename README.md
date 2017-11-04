# DALI python example
### Oliver McTammany

This entire project, from the first idea to planning to coding and commenting, took roughly an hour and a half. While it is not the most difficult project nor the cleanest code, I think this is a good demonstration of how I can execute on an idea and develop a working product in a short amount of time. It also demonstrates how much I pride myself on good comments, even when writing code that I never intended for anyone else to see. However, since I did not expect anyone else to play it, I did not code defensively, so be gentle.

The code is for the game MasterMind, where the user can either break the code or make the code. All interaction is via text. A sample game is below. Currently, line 16 prints the possibilities that the computer is considering so that the user can watch them get narrowed down before the comptuer arrives at the answer. If you want to test breaking the code, uncomment line 124 to have the computer tell you the code it generated.

#### Sample game
Hello! Type b to break the code or m to make the code!
> b


Okay, what do you guess?
> g b y o

r r 

Turn 2
> r b y o

r r 

Turn 3
> g b g o

r 

Turn 4
> r b b o

r w 

Turn 5
> b b y b

r r r 

Turn 6
> b b y y

r r w w 

Turn 7
> y b y b

You win! Congratulations!

Current score is you: 0, me: 7

To play again, type b to break the code or m to make it.
> m


Turn 1
I guess g, Y, o, o
> r w


Turn 2
I guess g, r, r, Y
> r r


Turn 3
I guess g, g, Y, Y
> r r w


Turn 4
I guess g, b, g, Y
> r r r r

I win! Thanks for playing!

Current score is you: 4, me: 7

To play again, type b to break the code or m to make it.

Pyhton FSA Lisp Program Generator

This program takes the Finite State Automata given via "fsa.txt", reads and parses the rules, and creates
a lisp program to check for legal and illegal string sequences. The python program reads "fsa.txt" which contains
a string of the FSA rules, parses the rules, and assigns lisp statements to each rule. The lisp statements will be
printed out to a new file called "part2.lsp". Running "part2.lsp" will read a fsa string to be tested from a .txt,
this file contains "theString.txt" which is a legal fsa. The lisp program will print out the string being tested and
if legal, will print that it the fsa is legal, if illegal then the program will print an error message regarding which
part of the fsa string is illegal. Created and tested on Visual Studio Code and Gitbash.

This folder contains xlwin32 which is the lisp environment I tested this program in. "p1.bat" and "p2.bat" load the xlwin32
environment with either "part1.lsp" or "part2.lsp" open ("p1.bat" will open "part1.lsp", "p2.bat" will open "part2.lsp"). "part1.lsp"
is a pre-made sample lisp file that is already correct and is what I used as a reference for how I wanted "part2.lsp" to be generated
as.

How to Run:
1.) Verify all files are present and within the same folder.
2.) Verify that if "part2.lsp" is present to delete that file, as the program generates a new one each time you run it.
3.) Open the "fsaParser.py" file (I used Visual Studio Code).
4.) In the command line run the command <python3 fsaParser.py fsa.txt> (not including '<>')
5.) The python program will generate "part2.lsp"
6.) Open the p2.bat file
7.) In the lisp program, enter the command <(demo)> (not including '<>')
8.) The lisp program will output the fsa string and whether or not it is legal or illegal and an error meessage.

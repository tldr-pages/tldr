# BLAHAJ

> A lolcat-like output colorizer tool that also prints flags and colorful sharks.
> More information: <https://codeberg.org/GeopJr/BLAHAJ>.

- Get a list of possible flags/colors:

`blahaj --flags`

- Print a shark (blahaj) with lesbian colors:

`blahaj -s --c lesbian`

- Print a random flag with a 2x size multiplier:

`blahaj --flag -r --multiplier 2`

- Print the result of a text-producing command with random colors:

`cowsay | blahaj -r`

- Echo text to console, color by individual character:

`echo "Hello, world" | blahaj -i`

- Print contents of text document, color by word, color background instead of text:

`blahaj -w -b path/to/file`

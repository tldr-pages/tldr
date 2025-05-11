# blahaj

> A lolcat-like output colorizer that also prints flags and colorful sharks.
> More information: <https://codeberg.org/GeopJr/BLAHAJ>.

- Get a list of possible flags/colors:

`blahaj --flags`

- Print a shark (blahaj) with default trans colors:

`blahaj {{[-s|--shark]}}`

- Print a random flag with a 2x size multiplier:

`blahaj {{[-f|--flag]}} {{[-r|--random]}} {{[-m|--multiplier]}} 2`

- Print the result of a text-producing command with lesbian colors:

`{{cowsay}} | blahaj {{[-c|--colors]}} lesbian`

- Echo text to console, color by individual character:

`echo "{{Hello, world}}" | blahaj {{[-i|--individual]}}`

- Print contents of text document, color by word, color background instead of text:

`blahaj {{[-w|--words]}} {{[-b|--background]}} {{path/to/file}}`

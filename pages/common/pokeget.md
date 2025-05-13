# pokeget

> Display sprites of Pokemon in your terminal.
> More information: <https://github.com/talwat/pokeget-rs>.

- Print a sprite of a given pokemon:

`pokeget {{pokemon_name}}`

- Print Mr. Mime (note the use of `-` instead of spaces):

`pokeget mr-mime`

- Print Mega Gengar:

`pokeget gengar {{[-m|--mega]}}`

- Print a random shiny Pokemon:

`pokeget random {{[-s|--shiny]}}`

- Print Alolan Meowth, without printing the Pokemon's name:

`pokeget meowth {{[-a|--alolan]}} --hide-name`

- Print a random Pokemon with 1/4096 chance to be shiny:

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`

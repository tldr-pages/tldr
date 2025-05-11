# pokeget

> Display sprites of Pokemon in your terminal, written in Rust.
> More information: <https://github.com/talwat/pokeget-rs>.

Print a given Pokemon sprite

`pokeget {{pokemon_name}}

- Print a female Pikachu:

`pokeget pikachu --female`

- Print Mega Gengar:

`pokeget gengar {{[-m|--mega]}}`

- Print a random shiny Pokemon:

`pokeget random {{[-s|--shiny]}}`

- Print an Alolan Meowth, without printing the Pokemon's name:

`pokeget meowth {{[-a|--alolan]}} --hide-name`

- Print a random Pokemon with 1/4096 chance to be shiny:

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`

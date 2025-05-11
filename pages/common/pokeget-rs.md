# pokeget

> Fetch Pokemon sprites, written in Rust.
> More information: <https://github.com/talwat/pokeget-rs>.

- Print a female Pikachu's sprite:

`pokeget pikachu --female`

- Print Mega Gengar's sprite:

`pokeget gengar --mega`

- Print a random shiny Pokemon's sprite:

`pokeget random --shiny`

- Print an Alolan Meowth, without printing the Pokemon's name:

`pokeget meowth --alolan --hide-name`

- Print a random Pokemon with 1/4096 chance to be shiny:

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`

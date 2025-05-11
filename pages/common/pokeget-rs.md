# pokeget-rs

> Fetch Pokemon sprites, written in rust.
> More information: <https://github.com/talwat/pokeget-rs>.

- Print a female Pikachu's sprite:

`pokeget pikachu --female`

- Print Mega Gengar's sprite

`pokeget gengar --mega`

- Print a random shiny pokemon's sprite

`pokeget random --shiny`

- Print an alolan meowth, without printing the pokemon's name

`pokeget meowth --alolan --hide-name`

- Print a random pokemon with 1/4096 chance to be shiny

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`

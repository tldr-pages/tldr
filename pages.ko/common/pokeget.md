# pokeget

> 터미널에 Pokemon 스프라이트 표시.
> 더 많은 정보: <https://github.com/talwat/pokeget-rs>.

- 지정한 pokemon의 스프라이트 출력:

`pokeget {{포켓몬_이름}}`

- Mr. Mime 출력 (공백 대싱 `-` 사용):

`pokeget mr-mime`

- Mega Gengar 출력:

`pokeget gengar {{[-m|--mega]}}`

- 무작위 shiny Pokemon 출력:

`pokeget random {{[-s|--shiny]}}`

- Pokemon 이름을 표시하지 않고 Alolan Meowth 출력:

`pokeget meowth {{[-a|--alolan]}} --hide-name`

- 1/4096 확률로 shiny가 되는 무작위 Pokemon 출력:

`((RANDOM%4096 == 0)) && pokeget random --shiny || pokeget random`

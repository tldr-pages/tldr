# exenv

> Egy eszköz az Elixir verziók egyszerű telepítéséhez és az alkalmazáskörnyezetek kezeléséhez. További információ: <https://github.com/exenv/exenv>.

- A telepített verziók listájának megjelenítése:

`exenv versions`

- Az Elixir egy adott verziójának használata az egész rendszerben:

`exenv global {{version}}`

- Az Elixir egy adott verziójának használata az aktuális alkalmazás/projekt könyvtárában:

`exenv local {{version}}`

- Az aktuálisan kiválasztott Elixir-verzió megjelenítése:

`exenv {{version}}`

- Az Elixir egy verziójának telepítése ( `elixir-build` plugin <https://github.com/mururu/elixir-build> szükséges [)](https://github.com/mururu/elixir-build):

`exenv install {{version}}`

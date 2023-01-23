# unset

> Héjváltozók vagy függvények eltávolítása. További információ: <https://manned.org/unset>.

- Távolítsa el a `foo` változót, vagy ha a változó nem létezik, távolítsa el a `foo` függvényt:

`unset {{foo}}`

- A foo és a bar változók eltávolítása:

`unset -v {{foo}} {{bar}}`

- Távolítsa el a my_func függvényt:

`unset -f {{my_func}}`

# atuin

> Tárolja a shell előzményeit egy kereshető adatbázisban. Opcionálisan szinkronizálhatja a titkosított előzményeket a gépek között. További információ: <https://atuin.sh/docs/overview/introduction/>.

- Telepítse az atuin-t a shelljébe:

`eval "$(atuin init {{bash|zsh|fish}})"`

- Importálja az előzményeket a shell alapértelmezett előzményfájljából:

`atuin import auto`

- Keresés a shell előzményekben egy adott parancsra:

`atuin search {{command}}`

- Regisztráljon fiókot az alapértelmezett szinkronizáló szerveren:

`atuin register -u {{username}} -e {{email}} -p {{password}}`

- Bejelentkezés az alapértelmezett szinkronizáló szerverre:

`atuin login -u {{username}} -p {{password}}`

- Előzmények szinkronizálása a szinkronizáló szerverrel:

`atuin sync`

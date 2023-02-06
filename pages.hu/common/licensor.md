# licensor

> Írjon engedélyeket a `stdout` címre. További információ: <https://github.com/raftario/licensor>.

- Írja az MIT licencet a `LICENSE` nevű fájlba:

`licensor {{MIT}} > {{LICENSE}}`

- Írja az MIT licencet egy \[p\]laceholder szerzői jogi megjegyzéssel a `LICENSE` nevű fájlba:

`licensor -p {{MIT}} > {{LICENSE}}`

- Adjon meg egy Bobby Tables nevű szerzői jogtulajdonost:

`licensor {{MIT}} {{"Bobby Tables"}} > {{LICENSE}}`

- A licenc kivételek megadása WITH kifejezéssel:

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- Az összes elérhető licenc felsorolása:

`licensor --licenses`

- List all available exceptions:

`licensor --exceptions`

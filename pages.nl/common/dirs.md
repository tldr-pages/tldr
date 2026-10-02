# dirs

> Toon of bewerk de stapel met mappen.
> De stapel met mappen is een lijst van recent bezochte mappen die kan worden bewerkt met de `pushd`- en `popd`-commando's.
> Zie ook: `pushd`, `popd`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Toon de stapel met mappen met een spatie tussen elke vermelding:

`dirs`

- Toon de stapel met mappen met één vermelding per regel:

`dirs -p`

- Toon een genummerde lijst van vermeldingen in de stapel met mappen:

`dirs -v`

- Toon de stapel met mappen zonder het tilde-voorvoegsel (`~`):

`dirs -l`

- Toon alleen de `n`-de vermelding in de stapel met mappen, beginnend bij 0 (alleen Bash):

`dirs +{{n}}`

- Toon alleen de `n`-de vermelding in de stapel met mappen vanaf het einde, beginnend bij 0 (alleen Bash):

`dirs -{{n}}`

- Wis de stapel met mappen:

`dirs -c`

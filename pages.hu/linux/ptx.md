# ptx

> Egy vagy több szövegfájlból egy vagy több szóból álló permutált index generálása. További információ: <https://www.gnu.org/software/coreutils/ptx>.

- Olyan permutált index generálása, ahol minden sor első mezője egy indexhivatkozás:

`ptx --references {{path/to/file}}`

- Permutált index generálása automatikusan generált indexhivatkozásokkal:

`ptx --auto-reference {{path/to/file}}`

- Permutált index generálása rögzített szélességgel:

`ptx --width={{width_in_columns}} {{path/to/file}}`

- Permutált index generálása szűrt szavak listájával:

`ptx --only-file={{path/to/filter}} {{path/to/file}}`

- Permutált index generálása SYSV-stílusú viselkedéssel:

`ptx --traditional {{path/to/file}}`

# tac

> Imprimați și concatenați fișierele în sens invers (ultima linie mai întâi).
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/tac>

- Imprimați conținutul fișierului1* inversat la ieșirea standard:

`tac {{file1}}`

- Imprimați conținutul intrării standard inversat la ieșirea standard:

`{{command}} | tac`

- Concatenează mai multe fișiere inversate în fișierul țintă:

`tac {{file1}} {{file2}} > {{target_file}}`

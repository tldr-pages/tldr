# unset

> Eliminați variabilele sau funcțiile shell.
> Mai multe informaţii: <https://manned.org/unset>

- Eliminați variabila `foo`, sau dacă variabila nu există, eliminați funcția `foo`:

`unset {{foo}}`

- Eliminați variabilele foo și bara:

`unset -v {{foo}} {{bar}}`

- Eliminați funcția my_func:

`unset -f {{my_func}}`

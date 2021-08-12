# at

> Execută comenzi la un moment specificat.
> Mai multe informaţii: <https://man.archlinux.org/man/at.1>

- Deschideți un prompt `at` pentru a crea un nou set de comenzi programate, apăsați `Ctrl + D` pentru a salva și a ieși:

`at {{hh:mm}}`

- Executați comenzile și trimiteți prin e-mail rezultatul folosind un program local de corespondență, cum ar fi sendmail:

`at {{hh:mm}} -m`

- Executați un script la momentul dat:

`at {{hh:mm}} -f {{path/to/file}}`

- Afișează o notificare de sistem la ora 11:00 pe 18 februarie:

`echo "notify-send '{{Wake up!}}'" | at {{11pm}} {{Feb 18}}`

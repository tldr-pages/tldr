# unison

> Instrument bidirecţional de sincronizare a fişierelor.
> Mai multe informaţii: <https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>

- Sincronizați două directoare (creează jurnal prima dată când aceste două directoare sunt sincronizate):

`unison {{path/to/directory_1}} {{path/to/directory_2}}`

- Acceptă automat valorile implicite (neconflictuale):

`unison {{path/to/directory_1}} {{path/to/directory_2}} -auto`

- Ignorați unele fișiere utilizând un model:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}`

- Afișează documentația:

`unison -doc {{topics}}`

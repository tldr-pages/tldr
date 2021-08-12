# fd

> O alternativă la „găsire'.
> Scopul este de a fi mai rapid și mai ușor de utilizat decât „găsi”.
> Mai multe informaţii: <https://github.com/sharkdp/fd>

- Găsirea recursivă a fișierelor care corespund modelului dat în directorul curent:

`fd {{pattern}}`

- Găsiți fișiere care încep cu „foo”:

`fd {{'^foo'}}`

- Găsiți fișiere cu o extensie specifică:

`fd --extension {{txt}}`

- Găsiți fișiere într-un anumit director:

`fd {{pattern}} {{path/to/directory}}`

- Includeți fișierele ignorate și ascunse în căutare:

`fd --hidden --no-ignore {{pattern}}`

- Executați o comandă pe fiecare rezultat de căutare returnat:

`fd {{pattern}} --exec {{command}}`

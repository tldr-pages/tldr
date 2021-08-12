# pamixer

> Un mixer simplu de linie de comandă pentru PulseAudio.
> Mai multe informaţii: <https://github.com/cdemoulins/pamixer>

- Listați toate chiuvetele și sursele cu ID-uri corespunzătoare:

`pamixer --list-sinks --list-sources`

- Setați volumul la 75% pe chiuveta implicită:

`pamixer --set-volume {{75}}`

- Comutați silențios pe o chiuvetă, alta decât cea implicită:

`pamixer --toggle-mute --sink {{ID}}`

- Măriți volumul pe chiuveta implicită cu 5%:

`pamixer --increase {{5}}`

- Reduceți volumul pe o sursă cu 5%:

`pamixer --decrease {{5}} --source {{ID}}`

- Utilizați opțiunea permite impuls pentru a mări, micșora sau seta volumul peste 100%:

`pamixer --set-volume {{105}} --allow-boost`

- Dezactivați chiuveta implicită (utilizați `—unmute` pentru a activa sunetul):

`pamixer --mute`

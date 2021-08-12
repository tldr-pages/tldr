# dunstify

> Un instrument de notificare care este o extensie a notificării, dar are mai multe caracteristici bazate în jurul dunst.
> Funcționează cu toate opțiunile care funcționează pentru notificare-trimitere.
> Mai multe informaţii: <https://wiki.archlinux.org/title/Dunst#Dunstify>

- Afișează o notificare cu un titlu și un mesaj dat:

`dunstify "{{Title}}" "{{Message}}"`

- Afișați o notificare cu urgență specificată:

`dunstify "{{Title}}" "{{Message}}" -u {{low|normal|critical}}`

- Specificați un ID de mesaj (suprascrie orice mesaje anterioare cu același ID):

`dunstify "{{Title}}" "{{Message}}" -r {{123}}`

- Pentru a vedea alte opțiuni posibile:

`notify-send --help`

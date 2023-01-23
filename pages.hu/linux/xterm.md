# xterm

> Terminál emulátor az X Window System számára. További információ: <https://manned.org/xterm>.

- Nyissa meg a terminált a `Example` címmel:

`xterm -T {{Example}}`

- A terminál megnyitása teljes képernyős módban:

`xterm -fullscreen`

- A terminál megnyitása sötétkék háttérrel és sárga előtérrel (betűszín):

`xterm -bg {{darkblue}} -fg {{yellow}}`

- Nyissa meg a terminált soronként 100 karakterrel és 35 sorral, x=200px, y=20px képernyőpozícióban:

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Nyissa meg a terminált Serif betűtípussal és 20-as betűmérettel:

`xterm -fa {{'Serif'}} -fs {{20}}`

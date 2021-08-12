# setxkbmap

> Setați tastatura utilizând Extensia Tastatură X.

- Setați tastatura în franceză AZERTY:

`setxkbmap {{fr}}`

- Setați mai multe machete de tastatură, variantele lor și opțiunea de comutare:

`setxkbmap -layout {{us,de}} -variant {{,qwerty}} -option {{'grp:alt_caps_toggle'}}`

- Adu ajutor:

`setxkbmap -help`

- Listează toate aspectele:

`localectl list-x11-keymap-layouts`

- Lista variantelor pentru aspect:

`localectl list-x11-keymap-variants {{de}}`

- Lista opțiunilor de comutare disponibile:

`localectl list-x11-keymap-options | grep grp:`

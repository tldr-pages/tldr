# maim

> Utilitar captură de ecran.
> Mai multe informaţii: <https://github.com/naelstrof/maim>

- Capturați o captură de ecran și salvați-o pe calea dată:

`maim {{path/to/screenshot.png}}`

- Capturați o captură de ecran a regiunii selectate:

`maim --select {{path/to/screenshot.png}}`

- Capturați o captură de ecran a regiunii selectate și salvați-o în clipboard (necesită `xclip`):

`maim --select | xclip -selection clipboard -target image/png`

- Capturează o captură de ecran a ferestrei active curente (necesită `xdotool`):

`maim --window $(xdotool getactivewindow) {{path/to/screenshot.png}}`

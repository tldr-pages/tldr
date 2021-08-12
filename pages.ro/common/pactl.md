# pactl

> Controlați un server de sunet PulseAudio care rulează.

- Lista tuturor chiuvete (sau alte tipuri - chiuvete sunt ieșiri și intrări chiuveta-sunt fluxuri audio active):

`pactl list {{sinks}} short`

- Schimbați chiuveta implicită (ieșire) la 1 (numărul poate fi recuperat prin subcomanda `list`):

`pactl set-default-sink {{1}}`

- Mutați chiuveta-intrare 627 să se scufunde 1:

`pactl move-sink-input {{627}} {{1}}`

- Setați volumul chiuvetei 1 la 75%:

`pactl set-sink-volume {{1}} {{0.75}}`

- Comutați mut pe chiuveta implicită (folosind numele special `@DEFAULT_SINK @`):

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`

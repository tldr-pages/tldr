# termdown

> Command-line Countdown-Timer.
> Weitere Informationen: <https://github.com/trehn/termdown>.

- Starte Stoppuhr:

`termdown`

- Starte einen Countdown von 1 Minute 30 Sekunden:

`termdown {{1m30s}}`

- Starte einen Countdown von 1 Minute 30 Sekunden. Nach ablauf der Zeit blinkt das Terminal:

`termdown 1m30s {{[-b|--blink]}}`

- Countdown mit Titel über der abgelaufenen Zeit:

`termdown {{1m30s}} {{[-T|--title]}} "{{Interesting title}}"`

- Zeige aktuelle Zeit:

`termdown {{[-z|--time]}}`

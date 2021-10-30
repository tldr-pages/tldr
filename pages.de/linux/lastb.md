# lastb

> Zeigt eine Liste der zuletzt angemeldeten Benutzer an.
> Weitere Informationen: <https://manned.org/lastb>.

- Zeige eine Liste aller zuletzt angemeldeten Benutzer an:

`sudo lastb`

- Zeige eine Liste aller zuletzt angemeldeten Benutzer seit einem bestimmten Zeitpunkt an:

`sudo lastb --since {{YYYY-MM-DD}}`

- Zeige eine Liste aller zuletzt angemeldeten Benutzer bis zu einem bestimmten Zeitpunkt an:

`sudo lastb --until {{YYYY-MM-DD}}`

- Zeige eine Liste aller angemeldeten Benutzer zu einem bestimmten Zeitpunkt an:

`sudo lastb --present {{hh:mm}}`

- Zeige eine Liste aller zuletzt angemeldeten Benutzer und übersetze die IP zu einem Hostnamen:

`sudo lastb --dns`

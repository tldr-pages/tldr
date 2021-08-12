# qutebrowser

> Un browser bazat pe tastatură, VIM-like bazat pe PyQt5.
> Mai multe informaţii: <https://qutebrowser.org/>

- Deschideți qutebrowser cu un director de stocare specificat:

`qutebrowser --basedir {{path/to/directory}}`

- Deschideți o instanță qutebrowser cu setări temporare:

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- Restaurați o sesiune numită a unei instanțe qutebrowser:

`qutebrowser --restore {{session_name}}`

- Lansați qutebrowser, deschizând toate adresele URL utilizând metoda specificată:

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- Deschideți qutebrowser cu un director de bază temporar și jurnalele de imprimare pentru a stdout ca JSON:

`qutebrowser --temp-basedir --json-logging`

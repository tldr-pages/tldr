# input

> Eseménykódok vagy érintőképernyős gesztusok küldése egy Android-eszközre. Ez a parancs csak a `adb shell` oldalon keresztül használható. További információ: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Egyetlen karakterhez tartozó eseménykód küldése egy Android-eszközre:

`input keyevent {{event_code}}`

- Szöveg küldése egy Android-eszközre (`%s` szóközöket jelöl):

`input text "{{text}}"`

- Egyetlen koppintás küldése egy Android-eszközre:

`input tap {{x_pos}} {{y_pos}}`

- Egy mozdulatsor küldése egy Android-eszközre:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Hosszú lenyomás küldése egy Android-eszközre egy lehúzó gesztus segítségével:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`

# xdotool

> Automatizare linie de comandă pentru X11.

- Recuperați ID-ul ferestrei (ferestrelor) Firefox care rulează:

`xdotool search --onlyvisible --name {{firefox}}`

- Faceți clic pe butonul din dreapta al mouse-ului:

`xdotool click {{3}}`

- Obțineți ID-ul ferestrei active în prezent:

`xdotool getactivewindow`

- Focus pe fereastra cu ID-ul de 12345:

`xdotool windowfocus --sync {{12345}}`

- Tastați un mesaj, cu o întârziere de 500 ms pentru fiecare literă:

`xdotool type --delay {{500}} "Hello world"`

- Apăsați tasta enter:

`xdotool key {{KP_Enter}}`

# rpmkeys

> Werkzeug um RPM Schüssel für RPM Repositories zu importieren oder löschen.
> Wenn ein RPM Repository hinzugefügt wird, dann muss man auch den entsprechend RPM Schüssel importieren.
> Mehr Informationen auf: <https://manpages.opensuse.org/Leap-15.6/man-pages-de/rpmkeys.8.de.html>.

- Liste alle importierte RMP Schüssel auf. Git auch die Schüssel ID aus welche beim späteren Löschen gebraucht wird:

`sudo rpmkeys {{[--list]}}`

- Entferne/Lösche eine zuvor importierten RMP Schüssel, angeben durch eine 16 stellige Nummer/Buchstaben Folge:

`sudo rpmkeys {{[--delete]}} {{[5a278d9c-5bbc73cb]}}`

- Importiere einen RPM Schüssel eines Repositories:

`sudo rpmkeys {{[--import]}} {{pfad_zu_schüssel_zum_importieren}}`

# xrandr

> Setzt die Auflösung, Orientierung und/oder Reflektion eines Bildschirmausgangs.
> Weitere Informationen: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Zeige den momentanen Systemzustand an (erkannte Bildschirme, Auflösungen, ...):

`xrandr --query`

- Deaktiviere nicht mehr verbundene Ausgangsgeräte und aktiviere verbundene Ausgänge mit Standardeinstellungen:

`xrandr --auto`

- Ändere die Auflösung und Bildfrequenz von DisplayPort 1 zu 1920x1080, 60Hz:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- Setze die Auflösung von HDMI auf 1280x1024 und platziere HDMI1 rechts von DP1:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- Deaktiviere den Ausgang von VGA1:

`xrandr --output {{VGA1}} --off`

- Setze die Bildschirmhelligkeit von LVDS1 auf 50%:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`

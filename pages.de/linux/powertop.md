# powertop

> Optimierung des Energieverbrauchs.
> Weitere Informationen: <https://github.com/fenrus75/powertop>.

- Kalibriere die Stromverbrauchsmessung:

`sudo powertop --calibrate`

- Erstelle einen HTML-Stromverbrauchsbericht im aktuellen Verzeichnis:

`sudo powertop --html={{stromverbrauchsbericht.html}}`

- Ermittle und wende die optimalen Einstellungen an:

`sudo powertop --auto-tune`

- Erstelle den Bericht für die gewünschte Dauer (statt der voreingestellten 20 Sekunden):

`sudo powertop --time={{5}}`

# xrandr

> Stel de grootte, oriëntatie en/of reflectie van de outputs voor een scherm in.
> Meer informatie: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Toon de huidige status van het systeem (bekende schermen, resoluties, ...):

`xrandr {{[-q|--query]}}`

- Schakel losgekoppelde outputs uit en schakel verbonden outputs aan met de standaardinstellingen:

`xrandr --auto`

- Wijzig de resolutie en updatefrequentie van DisplayPort 1 naar 1920x1080, 60Hz:

`xrandr --output DP1 --mode 1920x1080 {{[-r|--rate]}} 60`

- Stel de resolutie van HDMI2 in op 1280x1024 en plaats deze rechts van DP1:

`xrandr --output HDMI2 --mode 1280x1024 --right-of DP1`

- Schakel de VGA1 output uit:

`xrandr --output VGA1 --off`

- Stel de helderheid voor LVDS1 in op 50%:

`xrandr --output LVDS1 --brightness 0.5`

- Toon de huidige status van een X server:

`xrandr {{[-d|--display]}} :{{0}} {{[-q|--query]}}`

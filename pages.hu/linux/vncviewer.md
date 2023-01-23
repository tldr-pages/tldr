# vncviewer

> Elindít egy VNC (Virtual Network Computing) klienst. További információ: <https://manned.org/vncviewer>.

- Elindít egy VNC klienst, amely egy adott kijelzőn lévő állomáshoz csatlakozik:

`vncviewer {{host}}:{{display_number}}`

- Teljes képernyős módban történő indítás:

`vncviewer -FullScreen {{host}}:{{display_number}}`

- VNC-kliens indítása egy adott képernyőgeometriával:

`vncviewer --geometry {{width}}x{{height}} {{host}}:{{display_number}}`

- VNC-kliens indítása, amely egy adott porton csatlakozik egy állomáshoz:

`vncviewer {{host}}::{{port}}`

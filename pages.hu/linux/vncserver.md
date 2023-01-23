# vncserver

> Elindít egy VNC (Virtual Network Computing) asztalt. További információ: <https://manned.org/vncserver.1x>.

- VNC-kiszolgáló indítása a következő szabad kijelzőn:

`vncserver`

- VNC-kiszolgáló indítása meghatározott képernyőgeometriával:

`vncserver --geometry {{width}}x{{height}}`

- A VNC Server egy adott kijelzőn futó példányának kikapcsolása:

`vncserver --kill :{{display_number}}`

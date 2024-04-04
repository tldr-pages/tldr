# nixos-rebuild

> Rekonfiguriere eine NixOS-Maschine.
> Mehr Information: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Erstelle und wechsele zu einer neuen Konfiguration und starte diese zukünftig direkt:

`sudo nixos-rebuild switch`

- Erstelle und wechsele zu einer neuen Konfiguration und starte diese zukünftig direkt und bename diesen Start-Eintrag:

`sudo nixos-rebuild switch -p {{name}}`

- Erstelle und wechsele zu einer neuen Konfiguration und starte diese zukünftig direkt und installiere Updates:

`sudo nixos-rebuild switch --upgrade`

- Setze Änderungen der Konfiguration zurück und wechsle zur vorhergehenden Konfiguration:

`sudo nixos-rebuild switch --rollback`

- Erstelle eine neue Konfiguration und starte diese zukünftig direkt ohne sofort zu wechseln:

`sudo nixos-rebuild boot`

- Erstelle und wechsle direkt zu einer neuen Konfiguration, ändere den Standard-Start-Eintrag nicht (im Testfall):

`sudo nixos-rebuild test`

- Erstelle die Konfiguration und öffne diese in einer virtuellen Maschine:

`sudo nixos-rebuild build-vm`

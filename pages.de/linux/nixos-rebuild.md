# nixos-rebuild

> Rekonfiguriere eine NixOS-Maschine.
> Mehr Information: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Erstelle und wechsle zu einer neuen Konfiguration und nutze diese künftig als Standardkonfiguration:

`sudo nixos-rebuild switch`

- Gib der neu erstellten Standardkonfiguration einen Namen:

`sudo nixos-rebuild switch -p {{name}}`

- Erstelle und wechsle zu einer neuen Konfiguration, nutze diese künftig als Standardkonfiguration und installiere Updates:

`sudo nixos-rebuild switch --upgrade`

- Setze Änderungen der Konfiguration zurück und wechsle zur vorhergehenden Konfiguration:

`sudo nixos-rebuild switch --rollback`

- Erstelle eine neue Konfiguration und starte diese zukünftig direkt ohne sofort zu wechseln:

`sudo nixos-rebuild boot`

- Erstelle und wechsle direkt zu einer neuen Konfiguration, ändere den Standard-Start-Eintrag nicht (dieses Kommando ist für Testzwecke gedacht):

`sudo nixos-rebuild test`

- Erstelle die Konfiguration und öffne diese in einer virtuellen Maschine:

`sudo nixos-rebuild build-vm`

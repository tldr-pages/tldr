# nixos-rebuild

> Egy NixOS-gép újrakonfigurálása. További információ: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Készítse el és állítsa át az új konfigurációt, és tegye alapértelmezetté a rendszerindítást:

`sudo nixos-rebuild switch`

- Az új konfiguráció elkészítése és átállítása az új konfigurációra, a rendszerindítás alapértelmezetté tétele és a rendszerindító bejegyzés elnevezése:

`sudo nixos-rebuild switch -p {{name}}`

- Építés és váltás az új konfigurációra, a rendszerindítás alapértelmezetté tétele és a frissítések telepítése:

`sudo nixos-rebuild switch --upgrade`

- A konfiguráció módosításainak visszavétele, váltás az előző generációra:

`sudo nixos-rebuild switch --rollback`

- Az új konfiguráció létrehozása és a rendszerindítás alapértelmezetté tétele anélkül, hogy átállna rá:

`sudo nixos-rebuild boot`

- Az új konfiguráció létrehozása és aktiválása, de nem készít boot-bejegyzést (tesztelési céllal):

`sudo nixos-rebuild test`

- Készítse el a konfigurációt, és nyissa meg egy virtuális gépen:

`sudo nixos-rebuild build-vm`

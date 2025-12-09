# rpm

> RPM Package Manager.
> Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Meer informatie: <https://rpm-software-management.github.io/rpm/man/rpm.8>.

- Toon versie van het httpd-pakket:

`rpm {{[-q|--query]}} httpd`

- Toon versies van alle overeenkomende pakketten:

`rpm {{[-qa|--query --all]}} '{{mariadb*}}'`

- Installeer een pakket geforceerd, ongeacht de momenteel geïnstalleerde versies:

`rpm {{[-U|--upgrade]}} {{pad/naar/pakket.rpm}} --force`

- Identificeer de eigenaar van een bestand en toon de versie van het pakket:

`rpm {{[-qf|--query --file]}} {{/etc/postfix/main.cf}}`

- Toon bestanden die bij een pakket horen:

`rpm {{[-ql|--query --list]}} {{kernel}}`

- Toon scriptlets uit een RPM-bestand:

`rpm {{[-qp|--query --package]}} --scripts {{pakket.rpm}}`

- Toon gewijzigde, missende en/of onjuist geïnstalleerde bestanden van overeenkomende pakketten:

`rpm {{[-Va|--verify --all]}} '{{php-*}}'`

- Toon het changelog van een specifiek pakket:

`rpm {{[-q|--query]}} --changelog {{pakket}}`

# dnf install

> Installeer pakketten op Red Hat-gebaseerde distributies.
> Meer informatie: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Installeer pakketten op naam:

`sudo dnf {{[in|install]}} {{pakket1 pakket2 ...}}`

- Installeer een pakket vanuit een lokaal bestand:

`sudo dnf {{[in|install]}} {{pad/naar/bestand}}`

- Installeer een pakket vanaf het internet:

`sudo dnf {{[in|install]}} {{https://example.com/pakket.rpm}}`

- Voeg de Extra Packages for Enterprise Linux (EPEL) repositories toe:

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Voeg Remi's RPM repository toe:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`

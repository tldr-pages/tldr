# dnf install

> Installa pacchetti su distribuzioni basate su Red Hat.
> Maggiori informazioni: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Installa pacchetti per nome:

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- Installa un pacchetto da un file locale:

`sudo dnf {{[in|install]}} {{path/to/file}}`

- Installa un pacchetto da internet:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- Aggiunge il repository dei pacchetti non-free di Fedora:

`sudo dnf {{[in|install]}} https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm`

- Aggiunge i repository Extra Packages for Enterprise Linux (EPEL):

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Aggiunge il repository RPM di Remi:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`

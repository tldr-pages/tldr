# dnf install

> Red Hat tabanlı dağıtımlarda paket kurmak için kullanılır.
> Daha fazla bilgi için: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Paketleri ad ile kur:

`sudo dnf {{[in|install]}} {{paket1 paket2 ...}}`

- Yerel bir dosyadan paket kur:

`sudo dnf {{[in|install]}} {{yol/dosya}}`

- İnternetten bir paket kur:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- Extra Packages for Enterprise Linux (EPEL) depolarını ekle:

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Remi'nin RPM deposunu ekle:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`

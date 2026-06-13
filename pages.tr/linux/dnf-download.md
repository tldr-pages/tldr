# dnf download

> DNF depolarından RPM paketlerini indirir.
> Varsayılan olarak `dnf` ile gelmez, `dnf-plugins-core` ile desteklenir.
> Ayrıca bakınız: `dnf`.
> Daha fazla bilgi için: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Bir paketin en son sürümünü mevcut dizine indir:

`dnf download {{paket}}`

- Bir paketi belirli bir dizine indir (dizin mevcut olmalıdır):

`dnf download {{paket}} --destdir {{yol/dizin}}`

- RPM paketinin indirilebileceği URL'yi yazdır:

`dnf download --url {{paket}}`

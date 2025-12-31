# dnf builddep

> Belirli bir paketi derlemek için gerekli bağımlılıkları kurmak için kullanılır.
> Varsayılan olarak `dnf` ile gelmez, `dnf-plugins-core` ile desteklenir.
> Ayrıca bakınız: `dnf`.
> Daha fazla bilgi için: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- Belirli bir paket için bağımlılıkları kur:

`dnf builddep {{yol/tanım.spec}}`

- Belirli bir paket için bağımlılıkları kur, mevcut olmayanları yok say:

`dnf builddep --skip-unavailable {{yol/tanım.spec}}`

- RPM makrosunu belirli bir ifadeye ayarla:

`dnf builddep {{[-D|--define]}} '{{ifade}}'`

- `.spec` dosya yolu için bir argüman tanımla:

`dnf builddep --spec {{argüman}}`

- `.rpm` dosya yolu için bir argüman tanımla:

`dnf builddep --srpm {{argüman}}`

- Yardımı görüntüle:

`dnf builddep --help-cmd`

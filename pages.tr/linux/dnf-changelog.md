# dnf changelog

> Belirli bir paketin değişiklik kayıtlarını görüntülemek için kullanılır.
> Varsayılan olarak `dnf` ile gelmez, `dnf-plugins-core` ile desteklenir.
> Ayrıca bakınız: `dnf`.
> Daha fazla bilgi için: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- Belirli bir paketin tüm değişiklik kayıtlarını görüntüle:

`dnf changelog {{paket}}`

- Belirli bir paketin, belirli bir tarihten sonraki tüm değişiklik kayıtlarını görüntüle:

`dnf changelog --since {{tarih}} {{paket}}`

- Belirli bir paketin son `n` değişiklik kaydını görüntüle:

`dnf changelog --count {{sayi}} {{paket}}`

- Yalnızca yükseltilebilir paketler için yeni öğeleri göster:

`dnf changelog --upgrades {{paket}}`

- Yardımı görüntüle:

`dnf changelog --help-cmd`

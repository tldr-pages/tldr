# gitsome

> GitHub için gh komutuyla erişilebilen terminal tabanlı arayüz.
> Ayrıca `git` komutları için menu tarzı otomatik tamamlanmış öneriler sunar.
> Daha fazla bilgi için: <https://github.com/donnemartin/gitsome>.

- Otomatik tamamlamayı ve Git ile gh komutları için etkileşimli yardımı etkinleştirmek için gitsome kabuğuna gir:

`gitsome`

- Mevcut hesap ile GitHub entegrasyonunu ayarla:

`gh configure`

- Mevcut hesap için bildirimleri (https://github.com/notifications adresinde görülebildiği gibi) sırala:

`gh notifications`

- Mevcut hesabın yıldızlanan depolarını belirtilen filtre ile sırala:

`gh starred "{{python 3}}"`

- Belirtilen GitHub deposunun güncel etkileşimini görüntüle:

`gh feed {{tldr-pages/tldr}}`

- Belirtilen GitHub kullanıcısının güncel etkileşimini varsayılan sayfacı ile (örneğin `less`) göster:

`gh feed {{torvalds}} -p`

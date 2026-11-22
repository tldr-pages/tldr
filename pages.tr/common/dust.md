# dust

> Hangi dizinlerin disk alanı kullandığına dair anlık bir genel bakış sunun.
> Ayrıca bakınız: `du`, `ncdu`.
> Daha fazla bilgi: <https://github.com/bootandy/dust#usage>.

- Geçerli dizin için bilgileri görüntüle:

`dust`

- Bir veya daha fazla dizin hakkında bilgi görüntüle:

`dust {{dizin1/yolu dizin2/yolu ...}}`

- Toplam 30 dizini görüntüle (varsayılan değer 21):

`dust {{[-n|--number-of-lines]}} 30`

- Geçerli dizin için en fazla 3 seviye derinliğe kadar bilgi görüntüle:

`dust {{[-d|--depth]}} 3`

- En büyük dizinleri azalan sırada en üstte görüntüle:

`dust {{[-r|--reverse]}}`

- Bir dosyayı veya dizini yoksay:

`dust {{[-X|--ignore-directory]}} {{dosya_veya_dizin_yolu}}`

- Yüzde çubuklarını ve yüzdeleri görüntüleme:

`dust {{[-b|--no-percent-bars]}}`

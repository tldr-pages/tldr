# git tag

> Etiketleri oluştur, sırala, sil veya doğrula.
> Bir etiket, belirtilmiş bir commit'e bağlı statik bir referanstır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-tag>.

- Tüm etiketleri sırala:

`git tag`

- Belirtilen isim ile mevcut commit'e bağlı bir etiket yarat:

`git tag {{etiket_ismi}}`

- Belirtilen isim ile belirtilen commit'e bağlı bir etiket yarat:

`git tag {{etiket_ismi}} {{commit}}`

- Belirtilen mesaja sahip açıklamalı bir etiket yarat:

`git tag {{etiket_ismi}} -m {{etiket_mesajı}}`

- Belirtilen isimdeki etiketi sil:

`git tag -d {{etiket_ismi}}`

- Ana projeden güncellenmiş etiketleri al:

`git fetch --tags`

- Belirtilen commit'i içeren/içermiş tüm etiketleri sırala:

`git tag --contains {{commit}}`

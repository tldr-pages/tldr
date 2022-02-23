# git mv

> Dosyaları taşı veya yeniden adlandır ve Git indeksini güncelle.
> Daha fazla bilgi: <https://git-scm.com/docs/git-mv>.

- Depo içindeki dosyayı taşı ve bu hareketi sonraki commit'e ekle:

`git mv {{dosya/konumu}} {{yeni/dosya/konumu}}`

- Dosyayı yeniden adlandır ve yeniden adlandırma hareketini sonraki commit'e ekle:

`git mv {{dosya_ismi}} {{yeni_dosya_ismi}}`

- Eğer varsa belirtilen hedefteki dosyanın üstüne yaz:

`git mv --force {{dosya}} {{hedef}}`

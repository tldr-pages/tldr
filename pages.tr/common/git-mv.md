# git mv

> Dosyaları taşı veya yeniden adlandır ve Git indeksini güncelle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-mv>.

- Depo içindeki dosyayı taşı ve bu hareketi sonraki commit'e ekle:

`git mv {{yol/dosya}} {{yol/hedef}}`

- Dosyayı yeniden adlandır ve yeniden adlandırma hareketini sonraki commit'e ekle:

`git mv {{yol/dosya_veya_dizin}} {{yol/hedef}}`

- Eğer varsa belirtilen hedefteki dosyanın üstüne yaz:

`git mv {{[-f|--force]}} {{yol/dosya_veya_dizin}} {{yol/hedef}}`

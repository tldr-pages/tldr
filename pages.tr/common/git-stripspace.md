# git stripspace

> Gereksiz boşlukları sil.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stripspace>.

- Gereksiz boşlukları dosyadan kırp:

`cat {{yol/dosya}} | git stripspace`

- Gereksiz boşlukları ve Git yorumlarını dosyadan kırp:

`cat {{yol/dosya}} | git stripspace {{[-s|--strip-comments]}}`

- Bir dosyadaki tüm satırları Git yorumlarına çevir:

`git <{{yol/dosya}} stripspace {{[-c|--comment-lines]}}`

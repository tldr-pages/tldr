# git stripspace

> Gereksiz boşlukları sil.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stripspace>.

- Gereksiz boşlukları dosyadan kırp:

`cat {{örnek/dosya}} | git stripspace`

- Gereksiz boşlukları ve Git yorumlarını dosyadan kırp:

`cat {{örnek/dosya}} | git stripspace --strip-comments`

- Bir dosyadaki tüm satırları Git yorumlarına çevir:

`git stripspace --comment-lines < {{örnek/dosya}}`

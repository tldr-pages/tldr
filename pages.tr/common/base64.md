# base64

> Bir dosya veya standart veriyi Base64 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/base64>.

- Bir dosyayı şifrele:

`base64 {{dosyaismi}}`

- Bir dosyayı deşifre et:

`base64 --decode {{dosyaismi}}`

- stdin'den şifrele:

`{{herhangibirkomut}} | base64`

- stdin'den deşifre et:

`{{herhangibirkomut}} | base64 --decode`

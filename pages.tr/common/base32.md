# base32

> Bir dosya veya standart veriyi Base32 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
> Daha fazla bilgi: <https://www.gnu.org/software/coreutils/base32>.

- Bir dosyayı şifrele:

`base32 {{dosyaismi}}`

- Bir dosyayı deşifre et:

`base32 --decode {{dosyaismi}}`

- stdin'den şifrele:

`{{herhangibirkomut}} | base32`

- stdin'den deşifre et:

`{{herhangibirkomut}} | base32 --decode`

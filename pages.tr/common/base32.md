# base32

> Bir dosya veya standart veriyi Base32 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
> Daha fazla bilgi için: <https://manned.org/base32>.

- Bir dosyayı şifrele:

`base32 {{dosya/yolu}}`

- Kodlanmış çıktıyı belirli bir genişlikte sar (`0` sarmayı devre dışı bırakır):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{dosya/yolu}}`

- Bir dosyayı deşifre et:

`base32 {{[-d|--decode]}} {{dosya/yolu}}`

- `stdin`'den şifrele:

`{{herhangibirkomut}} | base32`

- `stdin`'den deşifre et:

`{{herhangibirkomut}} | base32 {{[-d|--decode]}}`

# base64

> Bir dosya veya standart veriyi Base64 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
> Daha fazla bilgi için: <https://manned.org/base64>.

- Bir dosyayı şifrele:

`base64 {{dosya/yolu}}`

- Kodlanmış çıktıyı belirli bir genişlikte sar (`0` sarmayı devre dışı bırakır):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{dosya/yolu}}`

- Bir dosyayı deşifre et:

`base64 {{[-d|--decode]}} {{dosya/yolu}}`

- `stdin`'den şifrele:

`{{herhangibirkomut}} | base64`

- `stdin`'den deşifre et:

`{{herhangibirkomut}} | base64 {{[-d|--decode]}}`

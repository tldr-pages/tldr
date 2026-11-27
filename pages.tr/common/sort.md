# sort

> Metin dosyalarının satırlarını sırala.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Bir dosyayı artan sırada sırala:

`sort {{yol/dosya}}`

- Bir dosyayı azalan sırada sırala:

`sort {{[-r|--reverse]}} {{yol/dosya}}`

- Bir dosyayı büyük/küçük harfe duyarsız şekilde sırala:

`sort {{[-f|--ignore-case]}} {{yol/dosya}}`

- Bir dosyayı alfabetik yerine sayısal sıraya göre sırala:

`sort {{[-n|--numeric-sort]}} {{yol/dosya}}`

- Alan ayırıcı olarak `:` kullanarak `/etc/passwd` dosyasını satırların 3. alanından itibaren sayısal olarak sırala:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3n /etc/passwd`

- Sayısal olarak 3. alana göre `/etc/passwd` dosyasını sırala, 3. alandaki değerler eşitse 4. alana göre üslü sayıları dikkate alarak sırala:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3,3n {{[-k|--key]}} 4,4g /etc/passwd`

- Bir dosyayı yalnızca benzersiz satırları koruyarak sırala:

`sort {{[-u|--unique]}} {{yol/dosya}}`

- Bir dosyayı sırala ve çıktıyı belirtilen çıktı dosyasına yaz (bir dosyayı yerinde sıralamak için kullanılabilir):

`sort {{[-o|--output]}} {{çıktı_dosyası/yolu}} {{girdi_dosyası/yolu}}`

# yes

> Bir şeyi tekrar tekrar yazdır.
> Bu komut genelde yükleme işlemleri sırasında onay için yes yazmak için kullanılır (`apt-get` gibi).
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Tekrar tekrar `y` yazdır:

`yes`

- Belirtilen bir değeri tekrar tekrar yazdır:

`yes {{değer}}`

- `apt-get` komutu tarafından sorulan her şeyi kabul et:

`yes | sudo apt-get install {{program}}`

- Bir istemdeki varsayılan seçeneği her zaman kabul etmek için tekrar tekrar yeni satır yazdır:

`yes ''`

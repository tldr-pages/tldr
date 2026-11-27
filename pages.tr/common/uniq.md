# uniq

> Bir girdideki veya dosyadaki benzersiz satırları yazdır.
> Tekrarlanan satırları yalnızca bitişik olduklarında algıladığı için önce satırları sıralamak gerekir.
> Ayrıca bakınız: `sort`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Tüm satırları yalnızca birer kez göster:

`sort {{yol/dosya}} | uniq`

- Yalnızca benzersiz satırları göster:

`sort {{yol/dosya}} | uniq {{[-u|--unique]}}`

- Yalnızca yinelenen satırları göster:

`sort {{yol/dosya}} | uniq {{[-d|--repeated]}}`

- Tüm satırları büyük/küçük harfe duyarsız şekilde yalnızca birer kez göster:

`sort {{yol/dosya}} | uniq {{[-i|--ignore-case]}}`

- Satırları, kaç kez geçtikleriyle birlikte göster:

`sort {{yol/dosya}} | uniq {{[-c|--count]}}`

- Satırları kaç kez geçtikleriyle birlikte, en sık geçenden başlayarak sıralı göster:

`sort {{yol/dosya}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`

- Benzersizlik için satırların yalnızca ilk 10 karakterini karşılaştır:

`sort {{yol/dosya}} | uniq {{[-w|--check-chars]}} 10`

- Benzersizlik için satırların ilk 5 karakterinden sonraki metni karşılaştır:

`sort {{yol/dosya}} | uniq {{[-s|--skip-chars]}} 5`

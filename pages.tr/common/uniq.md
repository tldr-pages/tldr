# uniq

> Bir girdideki veya dosyadaki benzersiz satırları yazdır.
> Tekrarlanan satırları yalnızca bitişik olduklarında algıladığı için önce satırları sıralamak gerekir.
> Ayrıca bakınız: `sort`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Tüm satırları yalnızca birer kez göster:

`sort {{dosya/yolu}} | uniq`

- Yalnızca benzersiz satırları göster:

`sort {{dosya/yolu}} | uniq {{[-u|--unique]}}`

- Yalnızca yinelenen satırları göster:

`sort {{dosya/yolu}} | uniq {{[-d|--repeated]}}`

- Tüm satırları büyük/küçük harfe duyarsız şekilde yalnızca birer kez göster:

`sort {{dosya/yolu}} | uniq {{[-i|--ignore-case]}}`

- Satırları, kaç kez geçtikleriyle birlikte göster:

`sort {{dosya/yolu}} | uniq {{[-c|--count]}}`

- Satırları kaç kez geçtikleriyle birlikte, en sık geçenden başlayarak sıralı göster:

`sort {{dosya/yolu}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`

- Benzersizlik için satırların yalnızca ilk 10 karakterini karşılaştır:

`sort {{dosya/yolu}} | uniq {{[-w|--check-chars]}} 10`

- Benzersizlik için satırların ilk 5 karakterinden sonraki metni karşılaştır:

`sort {{dosya/yolu}} | uniq {{[-s|--skip-chars]}} 5`

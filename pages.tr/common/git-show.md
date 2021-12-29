# git show

> Çeşitli Git nesnelerini (commit'ler, etiketler vs.) görüntüle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-show>.

- Son commit'e dair bilgi (değer, mesaj, değişimler ve öbür metaveriler) göster:

`git show`

- Belirtilen commit'e dair bilgi göster:

`git show {{commit}}`

- Belirtilen etiket ile özleşen commit'e dair bilgi göster:

`git show {{tag}}`

- Dalın HEAD'indeki 3. commit'e dair bilgi göster:

`git show {{dal}}~{{3}}`

- Commit'in mesajını diff çıktısını önleyerek tek satırda göster:

`git show --oneline -s {{commit}}`

- Yalnızca değiştirilen dosyalarla ilgili istatistik (eklenen/silinen karakterler) göster:

`git show --stat {{commit}}`

- Yalnızca eklenen, yeniden adlandırılan veya silinen dosyaların listesini göster:

`git show --summary {{commit}}`

- Bir dosyanın belirtilen sürümdeki (örneğin dal, etiket veya commit) içeriğini göster:

`git show {{sürüm}}:{{dosya/konumu}}`

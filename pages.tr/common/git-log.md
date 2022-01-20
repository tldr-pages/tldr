# git log

> Commit geçmişini göster.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-log>.

- Mevcut olandan başlayarak mevcut çalışma ortamındaki git deposunun commit silsilesini ters kronolojik düzende göster:

`git log`

- Belirtilen dosya veya dizinin tarihini farklılıklarla beraber göster:

`git log -p {{dosya/veya/dizin/konumu}}`

- Her bir commit'de hangi dosya(lar)ın değiştiğinin önizlemesini göster:

`git log --stat`

- Mevcut daldaki commit'lerin mesajlarının ilk satırını içeren bir çizelge göster:

`git log --oneline --graph`

- Bir depodaki commit, etiket ve dalların tamamını içeren bir çizelge göster:

`git log --oneline --decorate --all --graph`

- Mesajları yalnızca belirtilen ifadeleri içeren commit'leri göster (büyük-küçük harfe duyarsız):

`git log -i --grep {{aranan_ifade}}`

- Belirtilmiş yazardan gelen, belirtilen sayıda commit göster:

`git log -n {{sayı}} --author={{yazar}}`

- İki tarih arasında yapılmış commit'leri göster:

`git log --before={{tarih}} --after={{tarih}}`

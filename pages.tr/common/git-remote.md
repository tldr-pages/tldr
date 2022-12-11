# git remote

> İzlenen depolar dizisini (uzak bağlantıları) yönet.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-remote>.

- Varolan uzak bağlantıların isim ve URL'leriyle bir listesini göster:

`git remote -v`

- Uzak bağlantı ile ilgili bilgi göster:

`git remote show {{uzak_bağlantı_ismi}}`

- Uzak bağlantı ekle:

`git remote add {{uzak_bağlantı_ismi}} {{uzak_bağlantı_url'si}}`

- Uzak bağlantının URL'sini değiştir:

`git remote set-url {{uzak_bağlantı_ismi}} {{yeni_url}}`

- Uzak bağlantıyı sil:

`git remote remove {{uzak_bağlantı_ismi}}`

- Uzak bağlantıyı yeniden adlandır:

`git remote rename {{eski_isim}} {{yeni_isim}}`

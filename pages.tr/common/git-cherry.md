# git cherry

> Ana depoya aktarılması gereken commit'leri bul.
> Daha fazla bilgi: <https://git-scm.com/docs/git-cherry>.

- Commit'leri (ve mesajlarını) ana akımda kendilerine tekabül eden commit'ler ile göster:

`git cherry -v`

- Farklı bir ana akım ve konu dalı belirt:

`git cherry {{origin}} {{topic}}`

- Commit'leri verilen sınırlamalar ile sınırla:

`git cherry {{origin}} {{topic}} {{base}}`

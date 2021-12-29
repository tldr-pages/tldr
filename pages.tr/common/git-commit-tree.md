# git commit-tree

> Commit cisimleri oluşturmaya yarayan düşük seviyeli araç.
> Ayrıca `git commit` sayfasına bakılması önerilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-commit-tree>.

- Belirtilen mesaj ile bir commit cismi oluştur:

`git commit-tree {{ağaç}} -m "{{mesaj}}"`

- Bir dosyadan mesaj okuyan bir commit cismi oluştur (stdin için `-` ekini kullan):

`git commit-tree {{ağaç}} -F {{örnek/dosya}}`

- GPG anahtarıyla imzalanmış bir commit cismi oluştur:

`git commit-tree {{ağaç}} -m "{{mesaj}}" --gpg-sign`

- Belirtilen ana commit cismi ile bir commit cismi oluştur:

`git commit-tree {{ağaç}} -m "{{mesaj}}" -p {{ana_commit_sha}}`

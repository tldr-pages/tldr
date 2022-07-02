# git shortlog

> 'git log' çıktısını özetle.
> Daha fazla bilgi: <https://git-scm.com/docs/git-shortlog>.

- Yapılan tüm commit'lerin yazar ismiyle alfabetik olarak guruplanmış özetini göster:

`git shortlog`

- Yapılan tüm commit'lerin en çok commit yapan yazar ismi en üstte olacak şekilde özetini göster:

`git shortlog -n`

- Yapılan tüm commit'lerin yazar bilgilerini (isim ve e-posta) gösterecek şekilde özetini göster:

`git shortlog -c`

- En son yapılan 5 commit'in özetini göster (sürüm aralığı belirt):

`git shortlog HEAD~{{5}}..HEAD`

- Mevcut daldaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog -sne`

- Tüm dallardaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog -sne --all`

# git cherry-pick

> Varolan commit'ler ile getirilen yenilikleri mevcut dala uygula.
> Değişiklikleri başka bir dala aktarmak için, önce `git checkout` komutu kullanılmalıdır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-cherry-pick>.

- Mevcut dala bir commit uygula:

`git cherry-pick {{commit_ismi}}`

- Mevcut dala belirtilmiş aralıktaki kadar commit uygula (ayrıca `git rebase --onto` komutunun araştırılması önerilir):

`git cherry-pick {{ilk_commit}}~..{{son_commit}}`

- Mevcut dala birçok (ardışık olmayan) commit uygula:

`git cherry-pick {{commit_1}} {{commit_2}}`

- Bir commit'in değişikliklerini, herhangi bir yeni commit oluşturmadan çalışan dizine ekle:

`git cherry-pick -n {{commit}}`

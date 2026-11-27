# git fetch

> Uzak bir depodaki cisim ve referansları indir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-fetch>.

- Uzaktaki varsayılan ana akım depodan (eğer belirtildiyse) son değişiklikleri çek:

`git fetch`

- Belirtilen uzak ana akım depodan yeni dalları çek:

`git fetch {{uzak_bağlantı}}`

- Uzaktaki tüm ana akım depolardaki son değişiklikleri çek:

`git fetch --all`

- Uzaktaki ana akım depodan etiketleri dahi çek:

`git fetch {{[-t|--tags]}}`

- Ana akım depodan silinmiş uzak dallara giden yerel referansları sil:

`git fetch {{[-p|--prune]}}`

- Mevcut sığ (shallow) dalı 2 commit derinleştir:

`git fetch --deepen 2`

- Dal değiştirmeden `main` dalını güncelle (`git pull` ile eşdeğer):

`git fetch {{origin}} main:main`

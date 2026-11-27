# git worktree

> Aynı depoya bağlı çoklu çalışan ağaçları yönet.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-worktree>.

- Aynı ada sahip bir dal için yeni bir çalışma ağacı dizini ekle (dal yoksa oluşturulur):

`git worktree add {{dal}}`

- Belirtilen dala sahip yeni bir dizin yarat:

`git worktree add {{yol/dizin}} {{dal}}`

- Yeni bir dala sahip yeni bir dizin yarat:

`git worktree add {{yol/dizin}} -b {{yeni_dal}}`

- Tüm çalışma dizinlerini (ana dizin dahil) sırala:

`git worktree list`

- Var olan bir çalışma ağacını yeni bir konuma taşı:

`git worktree move {{yol/çalışma_ağacı}} {{yol/yeni_çalışma_ağacı}}`

- Bir çalışma ağacı dizinini ve meta verisini kaldır (sadece commit edilmemiş değişiklik yoksa):

`git worktree remove {{yol/çalışma_ağacı}}`

- Elle silinmiş bir çalışma ağacı dizininin meta verisini kaldır:

`git worktree prune`

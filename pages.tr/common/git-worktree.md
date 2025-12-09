# git worktree

> Aynı depoya bağlı çoklu çalışan ağaçları yönet.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-worktree>.

- Belirtilen dala sahip yeni bir dizin yarat:

`git worktree add {{örnek/dizin}} {{dal}}`

- Yeni bir dala sahip yeni bir dizin yarat:

`git worktree add {{örnek/dizin}} -b {{yeni_dal}}`

- Bu depoya bağlı tüm çalışan dizinleri sırala:

`git worktree list`

- Bir çalışma ağacını (çalışma ağacı dizinini sildikten sonra) kaldır:

`git worktree prune`

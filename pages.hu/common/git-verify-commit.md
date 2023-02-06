# git verify-commit

> A commitok GPG-ellenőrzésének ellenőrzése. Ha nincs ellenőrzött commit, akkor a megadott opcióktól függetlenül semmi sem lesz kiírva. További információ: <https://git-scm.com/docs/git-verify-commit>.

- A commitok ellenőrzése GPG aláírás szempontjából:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}}`

- A commitok ellenőrzése GPG aláírás szempontjából, és az egyes commitok részleteinek megjelenítése:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --verbose`

- A commitok ellenőrzése GPG aláírás szempontjából és a nyers részletek kiírása:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw`

# git verify-tag

> A címkék GPG ellenőrzésének ellenőrzése. Ha egy címke nem lett aláírva, hiba lép fel. További információ: <https://git-scm.com/docs/git-verify-tag>.

- A címkék GPG aláírás ellenőrzése:

`git verify-tag {{tag1 optional_tag2 ...}}`

- A címkék GPG-aláírás ellenőrzése és az egyes címkék részleteinek megjelenítése:

`git verify-tag {{tag1 optional_tag2 ...}} --verbose`

- A címkék ellenőrzése GPG aláírás szempontjából és a nyers részletek kinyomtatása:

`git verify-tag {{tag1 optional_tag2 ...}} --raw`

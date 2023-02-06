# git squash

> Több commit egyetlen commitba tömörítése. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- Egy adott ág összes commitjának egyesítése az aktuális ágba egyetlen commitként:

`git squash {{source_branch}}`

- Az aktuális ág egy adott commitjától kezdődő összes commit összevonása:

`git squash {{commit}}`

- Squash a `n` legújabb commitok és commit üzenettel:

`git squash HEAD~{{n}} "{{message}}"`

- Squash a `n` legújabb commitjai és az összes egyedi üzenetet összekapcsoló commit:

`git squash --squash-msg HEAD~{{n}}`

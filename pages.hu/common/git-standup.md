# git standup

> Egy adott felhasználó commitjainak megtekintése. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>.

- Megjeleníti egy adott szerző commitjait az elmúlt 10 napból:

`git standup -a {{name|email}} -d {{10}}`

- Megjeleníti egy adott szerző commitjait az elmúlt 10 napból, és azt, hogy azok GPG aláírással vannak-e ellátva:

`git standup -a {[name|email}} -d {{10}} -g`

- Az összes hozzájáruló összes commitjának megjelenítése az elmúlt 10 napban:

`git standup -a all -d {{10}}`

- Súgó megjelenítése:

`git standup -h`

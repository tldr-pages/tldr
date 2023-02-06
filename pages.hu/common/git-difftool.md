# git difftool

> Fájlváltozások megjelenítése külső diff eszközökkel. Ugyanazokat az opciókat és argumentumokat fogadja el, mint a `git diff`. Lásd még: `git diff`. További információ: <https://git-scm.com/docs/git-difftool>.

- Az elérhető diff eszközök listája:

`git difftool --tool-help`

- Az alapértelmezett diff eszköz beállítása a meldre:

`git config --global diff.tool "{{meld}}"`

- Az alapértelmezett diff eszköz használata a szakaszos változások megjelenítéséhez:

`git difftool --staged`

- Egy adott eszköz (opendiff) használata az adott commit óta történt változások megjelenítéséhez:

`git difftool --tool={{opendiff}} {{commit}}`

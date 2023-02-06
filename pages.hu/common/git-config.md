# git config

> A Git-tárházak egyéni konfigurációs beállításainak kezelése. Ezek a beállítások lehetnek helyi (az aktuális tárházra) vagy globális (az aktuális felhasználóra) konfiguráltak. További információ: <https://git-scm.com/docs/git-config>.

- Csak a helyi (az aktuális tárban a `.git/config` címen tárolt) konfigurációs bejegyzések listázása:

`git config --list --local`

- Csak a globális konfigurációs bejegyzések listázása (a `~/.gitconfig`) tárolva:

`git config --list --global`

- Csak a rendszerkonfigurációs bejegyzéseket listázza (a `/etc/gitconfig`), és megmutatja a fájljuk helyét:

`git config --list --system --show-origin`

- Egy adott konfigurációs bejegyzés értékének lekérdezése:

`git config alias.unstage`

- Egy adott konfigurációs bejegyzés globális értékének beállítása:

`git config --global alias.unstage "reset HEAD --"`

- Egy globális konfigurációs bejegyzés alapértelmezett értékének visszaállítása:

`git config --global --unset alias.unstage`

- Az aktuális tárolóhely Git-konfigurációjának szerkesztése az alapértelmezett szerkesztőprogramban:

`git config --edit`

- A globális Git-konfiguráció szerkesztése az alapértelmezett szerkesztőben:

`git config --global --edit`

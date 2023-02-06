# git for-each-repo

> Git parancs futtatása a tárolók listáján. Megjegyzés: ez a parancs kísérleti jellegű és változhat. További információ: <https://git-scm.com/docs/git-for-each-repo>.

- Karbantartás futtatása a `maintenance.repo` felhasználói konfigurációs változóban tárolt tárolók listájának minden egyes tárolóján:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- A `git pull` futtatása a globális konfigurációs változóban felsorolt minden egyes tárolón:

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`

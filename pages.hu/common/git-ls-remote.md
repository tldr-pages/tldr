# git ls-remote

> Git parancs egy távoli repositoryban lévő hivatkozások listázására név vagy URL alapján. Ha nincs név vagy URL megadva, akkor a konfigurált upstream ágat fogja használni, vagy a távoli eredetet, ha az előbbi nincs konfigurálva. További információ: <https://git-scm.com/docs/git-ls-remote>.

- Az alapértelmezett távoli tárolóban lévő összes hivatkozás megjelenítése:

`git ls-remote`

- Csak az alapértelmezett távoli adattárban lévő fejhivatkozások megjelenítése:

`git ls-remote --heads`

- Csak a címkehivatkozások megjelenítése az alapértelmezett távoli tárolóban:

`git ls-remote --tags`

- Az összes távoli tárolóból származó hivatkozás megjelenítése név vagy URL alapján:

`git ls-remote {{repository_url}}`

- Távoli adattárból származó hivatkozások megjelenítése egy minta alapján szűrve:

`git ls-remote {{repository_name}} "{{pattern}}"`

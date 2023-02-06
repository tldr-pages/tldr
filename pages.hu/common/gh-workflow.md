# gh workflow

> A GitHub Actions munkafolyamatok listázása, megtekintése és futtatása. További információ: <https://cli.github.com/manual/gh_workflow>.

- Interaktívan kiválaszthat egy munkafolyamatot a legutóbbi munkák megtekintéséhez:

`gh workflow view`

- Egy adott munkafolyamat megtekintése az alapértelmezett böngészőben:

`gh workflow view {{id|workflow_name|filename.yml}} --web`

- Egy adott munkafolyamat YAML definíciójának megjelenítése:

`gh workflow view {{id|workflow_name|filename.yml}} --yaml`

- Egy adott Git-ág vagy címke YAML-definíciójának megjelenítése:

`gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}} --yaml`

- Munkafolyamat-fájlok listázása (a `--all` használatával a letiltott munkafolyamatok is szerepelhetnek):

`gh workflow list`

- Kézi munkafolyamat futtatása paraméterekkel:

`gh workflow run {{id|workflow_name|filename.yml}} --raw-field {{param1}}={{value1}} --raw-field {{param2}}={{value2}}`

- Kézi munkafolyamat futtatása egy adott ág vagy címke használatával JSON paraméterekkel a `stdin` oldalról:

`echo '{{{"param1":"value1", "param2":"value2"}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}}`

- Egy adott munkafolyamat engedélyezése vagy letiltása:

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`

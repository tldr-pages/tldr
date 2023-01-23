# core-validate-commit

> A Node.js maghoz tartozó commit üzenetek hitelesítése. További információ: <https://github.com/nodejs/core-validate-commit>.

- Az aktuális commit hitelesítése:

`core-validate-commit`

- Egy adott commit hitelesítése:

`core-validate-commit {{commit_hash}}`

- Commitek egy tartományának érvényesítése:

`git rev-list {{commit_hash}}..HEAD | xargs core-validate-commit`

- Az összes érvényesítési szabály listázása:

`core-validate-commit --list`

- Az összes érvényes Node.js alrendszer felsorolása:

`core-validate-commit --list-subsystem`

- Az aktuális commit érvényesítése A kimenet formázása csap formátumban:

`core-validate-commit --tap`

- Súgó megjelenítése:

`core-validate-commit --help`

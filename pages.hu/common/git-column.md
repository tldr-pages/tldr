# git column

> Az adatok oszlopokban történő megjelenítése. További információ: <https://git-scm.com/docs/git-column>.

- A szabványos bemenet több oszlopként történő formázása:

`ls | git column --mode={{column}}`

- A szabványos bemenet több oszlopként történő formázása, maximális szélessége `100`:

`ls | git column --mode=column --width={{100}}`

- A szabványos bemenet több oszlopként történő formázása, legfeljebb `30` kitöltéssel:

`ls | git column --mode=column --padding={{30}}`

# recsel

> Rekordok nyomtatása egy recfile-ból: egy ember által szerkeszthető, egyszerű szöveges adatbázisból. További információ: <https://www.gnu.org/software/recutils/manual/recutils.html>.

- Név és verzió mező kivonása:

`recsel -p name,version {{data.rec}}`

- Használja a "~" karakterláncnak egy adott reguláris kifejezéssel való megfeleltetésére:

`recsel -e "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"`

- Használjon predikátumot a név és a verzió egyezéséhez:

`recsel -e "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}`

# ndctl

> Segédprogram a nem-olatilis DIMM-ek kezeléséhez. További információ: <https://manned.org/ndctl>.

- Hozzon létre egy 'fsdax' üzemmódú névteret:

`ndctl create-namespace --mode={{fsdax}}`

- Egy névtér üzemmódjának megváltoztatása 'raw'-ra:

`ndctl create-namespace --reconfigure={{namespaceX.Y}} --mode={{raw}}`

- Ellenőrizze a szektor módú névtér konzisztenciáját, és szükség esetén javítsa ki:

`ndctl check-namespace --repair {{namespaceX.Y}}`

- Az összes névtér, régió és busz listázása (beleértve a letiltottakat is):

`ndctl list --namespaces --regions --buses --idle`

- Egy adott névtér listázása és sok további információ hozzáadása:

`ndctl list -vvv --namespace={{namespaceX.Y}}`

- Monitor futtatása az "ACPI.NFIT" buszon lévő NVDIMM-ek SMART állapotjelző eseményeinek figyelésére:

`ndctl monitor --bus={{ACPI.NFIT}}`

- Egy névtér eltávolítása (ha alkalmazható) vagy visszaállítása kezdeti állapotba:

`ndctl destroy-namespace --force {{namespaceX.Y}}`

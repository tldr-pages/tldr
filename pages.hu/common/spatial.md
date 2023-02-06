# spatial

> A SpatialOS projektek kezeléséhez és fejlesztéséhez szükséges parancsok készlete. További információ: <https://ims.improbable.io/products/spatialos>.

- Futtassa ezt, amikor először használ egy projektet:

`spatial worker build`

- Munkások építése a helyi telepítéshez a Unityn macOS-en:

`spatial worker build --target=development --target=Osx`

- Build workers for local deployment on Unreal on Windows:

`spatial worker build --target=local --target=Windows`

- Helyi telepítés:

`spatial local launch {{launch_config}} --snapshot={{snapshot_file}}`

- Indítson el egy helyi munkást a helyi telepítéshez való csatlakozáshoz:

`spatial local worker launch {{worker_type}} {{launch_config}}`

- Összeállítás feltöltése a felhőalapú telepítésekhez:

`spatial cloud upload {{assembly_name}}`

- Felhőalapú telepítés indítása:

`spatial cloud launch {{assembly_name}} {{launch_config}} {{deployment_name}}`

- Munkavállalói könyvtárak tisztítása:

`spatial worker clean`

# meshlabserver

> A MeshLab 3D hálófeldolgozó szoftver parancssori interfésze. További információ: <https://manned.org/meshlabserver>.

- STL fájl átalakítása OBJ fájlba:

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- WRL fájl konvertálása OFF fájlba, beleértve a kimeneti hálóban lévő csúcs- és arcnormálokat is:

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- Az összes rendelkezésre álló feldolgozási szűrő listájának egy fájlba történő kiírása:

`meshlabserver -d {{path/to/file}}`

- 3D fájl feldolgozása a MeshLab GUI-ban létrehozott szűrőszkript segítségével (Szűrők > Aktuális szűrőszkript megjelenítése > Szkript mentése):

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- 3D fájl feldolgozása egy szűrőszkript segítségével, a szűrők kimenetét egy naplófájlba írva:

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`

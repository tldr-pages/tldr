# meshlabserver

> Interfață linie de comandă pentru software-ul de procesare a meshlab 3D.

- Conversia unui fişier STL într-un fişier OBJ:

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- Conversia unui fișier WRL într-un fișier OFF, inclusiv nodul și față normalele din plasa de ieșire:

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- Dump o listă cu toate filtrele de procesare disponibile într-un fișier:

`meshlabserver -d {{filename}}`

- Procesați un fișier 3D utilizând un script de filtrare creat în interfața grafică MeshLab (Filtre > Afișați script-ul curent de filtrare > Salvare script):

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- Procesați un fișier 3D utilizând un script de filtrare, scriind ieșirea filtrelor într-un fișier jurnal:

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`

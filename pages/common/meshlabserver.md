# meshlabserver

> Command line interface for the MeshLab 3D mesh processing software.

- Convert an STL file to an OBJ file:

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- Convert a WRL file to a OFF file, including the vertex and face normals in the output mesh:

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- Dump a list of all the available processing filters into a file:

`meshlabserver -d {{filename}}`

- Process a 3D file using a filter script created in the MeshLab GUI (Filters > Show current filter script > Save Script):

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- Process a 3D file using a filter script, writing the output of the filters into a log file:

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`

# meshlabserver

> Ինտերֆեյս MeshLab 3D ցանցերի մշակման ծրագրաշարի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/meshlabserver>:.

- Վերափոխեք STL ֆայլը OBJ ֆայլի.:

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- Փոխակերպեք WRL ֆայլը OFF ֆայլի, ներառյալ գագաթնակետը և դեմքի նորմալները ելքային ցանցում.:

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- Թափել բոլոր առկա մշակման ֆիլտրերի ցանկը ֆայլի մեջ.:

`meshlabserver -d {{path/to/file}}`

- Մշակեք 3D ֆայլ՝ օգտագործելով MeshLab GUI-ում ստեղծված զտիչ սկրիպտը (Զտիչներ > Ցույց տալ ընթացիկ ֆիլտրի սցենարը > Պահպանել սցենարը):

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- Մշակեք 3D ֆայլ՝ օգտագործելով զտիչ սկրիպտ՝ գրելով ֆիլտրերի ելքը գրանցամատյանում.:

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`

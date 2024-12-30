# meshlabserver

> MeshLab 3D网格处理软件的命令行界面。
> 更多信息：<https://manned.org/meshlabserver>。

- 将STL文件转换为OBJ文件：

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- 将WRL文件转换为OFF文件，包括输出网格中的顶点和面法线：

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- 将所有可用的处理过滤器列表转储到一个文件中：

`meshlabserver -d {{path/to/file}}`

- 使用在MeshLab GUI中创建的过滤器脚本处理3D文件（过滤器 > 显示当前过滤器脚本 > 保存脚本）：

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- 使用过滤器脚本处理3D文件，将过滤器的输出写入日志文件：

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`
# meshlabserver

> MeshLab 3D 网格处理软件的命令行接口。
> 更多信息：<https://manned.org/meshlabserver>。

- 将 STL 文件转换为 OBJ 文件：

`meshlabserver -i {{input.stl}} -o {{output.obj}}`

- 将 WRL 文件转换为 OFF 文件，包括输出网格中的顶点和面法线：

`meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn`

- 将所有可用处理滤镜的列表导出到文件中：

`meshlabserver -d {{path/to/file}}`

- 使用在 MeshLab GUI (滤镜 > 显示当前滤镜脚本 > 保存脚本) 中创建的滤镜脚本处理 3D 文件：

`meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}`

- 使用滤镜脚本处理 3D 文件，并将滤镜的输出写入日志文件：

`meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}`

# Godot

> 一个开源的2D和3D游戏引擎。
> 更多信息：<https://godotengine.org/>

- 如果当前目录包含 `project.godot` 文件，则运行项目；否则打开项目管理器：

`godot`

- 编辑项目（当前目录必须包含 `project.godot` 文件）：

`godot -e`

- 即使当前目录包含 `project.godot` 文件，也打开项目管理器：

`godot -p`

- 为给定的导出预设导出项目（预设必须在项目中定义）：

`godot --export {{preset}} {{output_path}}`

- 执行独立的 GDScript 文件（脚本必须继承自 `SceneTree` 或 `MainLoop`）：

`godot -s {{script.gd}}`
# yolo

> YOLO 命令行界面让你可以简单地在不同的任务和版本上进行模型的训练、验证或推理。
> 更多信息：<https://docs.ultralytics.com/cli/>.

- 在当前工作目录中创建默认配置的副本：

`yolo task=init`

- 使用指定的配置文件训练目标检测、实例分割或分类模型：

`yolo task={{detect|segment|classify}} mode=train cfg={{路径/到/config.yaml}}`

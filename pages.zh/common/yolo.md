# yolo

> YOLO 命令行界面让您可以简单地在各种任务和版本上训练、验证或推断模型。
> 更多信息：<https://docs.ultralytics.com/cli/>。

- 在您当前的工作目录中创建默认配置的副本：

`yolo task=init`

- 使用指定的配置文件训练目标检测、实例分割或分类模型：

`yolo task={{detect|segment|classify}} mode=train cfg={{path/to/config.yaml}}`
# yolo

> The YOLO command line interface lets you simply train, validate or infer models on various tasks and versions.
> More information: <https://docs.ultralytics.com/cli/>.

- Create a copy of the default configuration in your current working directory:

`yolo task=init`

- Train the object detection, instance segment, or classification model with the specified configuration file:

`yolo task={{detect|segment|classify}} mode=train cfg={{path/to/config.yaml}}`

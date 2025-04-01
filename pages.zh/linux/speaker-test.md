# speaker-test

> 用于 ALSA 的扬声器测试音生成器。
> 参见：`aplay`, `arecord`, `amixer`。
> 更多信息：<https://manned.org/speaker-test>。

- 使用粉红噪音测试默认扬声器：

`speaker-test`

- 使用正弦波测试默认扬声器：

`speaker-test {{[-t|--test]}} sine {{[-f|--frequency]}} {{frequency}}`

- 使用预定义的 WAV 文件测试默认扬声器：

`speaker-test {{[-t|--test]}} wav`

- 使用指定的 WAV 文件测试默认扬声器：

`speaker-test {{[-t|--test]}} wav {{[-w|--wavfile]}} {{path/to/file}}`

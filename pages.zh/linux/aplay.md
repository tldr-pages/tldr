# aplay

> ALSA 声卡驱动的音频播放器。
> 更多信息请访问：<https://manned.org/aplay>。

- 播放指定文件（采样率、位深度等将自动根据文件格式确定）：

`aplay {{path/to/file}}`

- 以 2500 Hz 播放指定文件的前 10 秒：

`aplay --duration={{10}} --rate={{2500}} {{path/to/file}}`

- 将原始文件作为 22050 Hz、单声道、8 位、Mu-Law `.au` 文件播放：

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{path/to/file}}`
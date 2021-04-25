# aplay

> ALSA 声卡驱动程序的命令行声音播放器。
> 更多信息：<https://manned.org/aplay>.

- 播放一个文件（会自动根据文件格式确定采样率、位深等）：

`aplay {{文件路径}}`

- 以 2500 Hz 播放指定文件的前 10 秒：

`aplay --duration={{10}} --rate={{2500}} {{文件路径}}`

- 以 22050 Hz，mono，8-bit，Mu-Law 和 `.au` 格式来播放指定原始文件：

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{文件路径}}`

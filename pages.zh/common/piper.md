# piper

> 一个快速的本地神经文本转语音系统。
> 从 <https://rhasspy.github.io/piper-samples> 尝试和下载语音模型。
> 更多信息请访问：<https://github.com/rhasspy/piper>。

- 使用文本转语音模型输出一个WAV [f]ile（假设配置文件位于 model_path + .json）：

`echo {{要说的话}} | piper -m {{path/to/model.onnx}} -f {{outputfile.wav}}`

- 使用模型并指定其JSON [c]onfig文件输出一个WAV [f]ile：

`echo {{'要说的话'}} | piper -m {{path/to/model.onnx}} -c {{path/to/model.onnx.json}} -f {{outputfile.wav}}`

- 通过指定说话者的ID号选择多个说话者中的特定说话者：

`echo {{'为什么？'}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{angry.wav}}`

- 将输出流发送到mpv媒体播放器：

`echo {{'你好，世界'}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- 以两倍的速度说话，句子之间有很大的间隔：

`echo {{'以两倍的速度说话。增加戏剧性！'}} | piper -m {{foo.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{drama.wav}}`
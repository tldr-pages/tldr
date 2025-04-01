# piper

> 一个快速的本地神经文本转语音系统。
> 尝试使用和下载语音模型：<https://rhasspy.github.io/piper-samples>。
> 更多信息：<https://github.com/rhasspy/piper>。

- 使用文本转语音模型输出一个 WAV 文件（假设模型路径后面是 .json 配置文件）：

`echo {{要说话的内容}} | piper -m {{模型路径/model.onnx}} -f {{输出文件.wav}}`

- 使用模型及其 JSON 配置文件输出一个 WAV 文件：

`echo {{'要说话的内容'}} | piper -m {{模型路径/model.onnx}} -c {{模型路径/model.onnx.json}} -f {{输出文件.wav}}`

- 通过指定说话人的 ID 号码，在包含多个说话人声音中选择特定说话人：

`echo {{'为什么？'}} | piper -m {{de_DE-thorsten_emotional-medium.onnx}} --speaker {{1}} -f {{生气.wav}}`

- 将输出流式传输到 mpv 媒体播放器：

`echo {{'你好，世界'}} | piper -m {{en_GB-northern_english_male-medium.onnx}} --output-raw -f - | mpv -`

- 以两倍速说话，并在句子间留出很大的停顿：

`echo {{'说话速度加倍。增加戏剧效果！'}} | piper -m {{foo.onnx}} --length_scale {{0.5}} --sentence_silence {{2}} -f {{戏剧.wav}}`
# 语音合成

> 合成语音。
> 更多信息：<https://github.com/coqui-ai/TTS#command-line-tts>。

- 使用默认模型运行文本转语音，将输出写入“tts_output.wav”：

`tts --text "{{text}}"`

- 列出提供的模型：

`tts --list_models`

- 按索引查询模型信息：

`tts --model_info_by_idx {{model_type/model_query_idx}}`

- 按名称查询模型信息：

`tts --model_info_by_name {{model_type/language/dataset/model_name}}`

- 使用其默认声码器模型运行一个文本到语音模型：

`tts --text "{{text}}" --model_name {{model_type/language/dataset/model_name}}`

- 运行您自己的文本到语音模型（使用Griffin-Lim声码器）：

`tts --text "{{text}}" --model_path {{path/to/model.pth}} --config_path {{path/to/config.json}} --out_path {{path/to/file.wav}}`
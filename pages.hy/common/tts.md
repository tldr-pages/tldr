# tts

> Սինթեզել խոսքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/coqui-ai/TTS#command-line-tts>:.

- Գործարկեք տեքստը-խոսք լռելյայն մոդելներով՝ ելքը գրելով «tts_output.wav»:

`tts --text "{{text}}"`

- Ներկայացված մոդելների ցանկ.:

`tts --list_models`

- Հարցման տեղեկատվություն մոդելի համար idx-ով.:

`tts --model_info_by_idx {{model_type/model_query_idx}}`

- Անունով մոդելի մասին տեղեկություն.:

`tts --model_info_by_name {{model_type/language/dataset/model_name}}`

- Գործարկեք տեքստից խոսքի մոդել իր լռելյայն ձայնակոդավորիչ մոդելով.:

`tts --text "{{text}}" --model_name {{model_type/language/dataset/model_name}}`

- Գործարկեք ձեր սեփական տեքստի խոսքի մոդելը (օգտագործելով Griffin-Lim ձայնագրիչը).:

`tts --text "{{text}}" --model_path {{path/to/model.pth}} --config_path {{path/to/config.json}} --out_path {{path/to/file.wav}}`

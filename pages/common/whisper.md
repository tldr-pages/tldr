# whisper

> CLI tool to convert audio files to txt,vtt,srt,tsv,json.
> More information: <https://github.com/openai/whisper>.

- Convert a specific audio file to all of the given file formats:

`whisper {{path/to/audio.mp3}}`

- Convert an audio file specifying the output format of the converted file:

`whisper {{path/to/audio.mp3}} --output_format {{txt}}`

- Convert an audio file using a specific model for conversion:

`whisper {{path/to/audio.mp3}} --model {{tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}}`

- Convert an audio file specifying which language the audio file is in to reduce conversion time:

`whisper {{path/to/audio.mp3}} --language {{english}}`

- Convert an audio file and save it to a specific location:

`whisper {{path/to/audio.mp3}} --output_dir "{{path/to/output}}"`

- Convert an audio file in quiet mode:

`whisper {{path/to/audio.mp3}} --verbose {{False}}`

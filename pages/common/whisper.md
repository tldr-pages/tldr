# whisper

> CLI tool to convert audio files to txt,vtt,srt,tsv,json.
> More information: <https://github.com/openai/whisper>.

- Convert the audio file named audio.mp3 to all of the given file formats:

`whisper {{path/to/audio.mp3}}`

- Specify the output format of the converted file:

`whisper {{path/to/audio.mp3}} --output-format {{txt}}`

- Specify which model to use for conversion:

`whisper {{path/to/audio.mp3}} --model {{tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}}`

- Specify which language the audio file is in to reduce conversion time:

`whisper {{path/to/audio.mp3}} --language {{english}}`

- Specify where to save the converted files:

`whisper {{path/to/audio.mp3}} --output_dir "{{path/to/output}}"`

- Change the verbose settings of whisper:

`whisper {{path/to/audio.mp3}} --verbose {{False}}`

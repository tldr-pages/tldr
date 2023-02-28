# whisper

> CLI tool to convert audio files to txt,vtt,srt,tsv,json.
> Read more: <https://github.com/openai/whisper>.

- Convert audio file named audio.mp3 to all of the given file formats:

`whisper {{path/to/audio.mp3}}`

- Specify only which file to generate:

`whisper {{path/to/audio.mp3}} --output-format {{txt}}`

- Specify which model to use (models:- tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large):

`whisper {{path/to/audio.mp3}} --model {{tiny}}`

- Specify which language the audio file is to reduce time:

`whisper {{path/to/audio.mp3}} --language {{english}}`

- Specify where to save the converted files:

`whisper {{path/to/audio.mp3}} --output_dir "{{path/to/output}}"`

- Change the verbose settings of whisper:

`whisper {{path/to/audio.mp3}} --verbose {{False}}`

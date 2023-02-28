# whisper

> CLI tool to convert audio files to txt,vtt,srt,tsv,json.
> Created By OpenAI. Read more:- https://github.com/openai/whisper

- Convert audio file named audio.mp3 to all of the given file formats:

`whisper audio.mp3`

- Specify only which file to generate:

`whisper audio.mp3 --output-format txt`

- Specify which model to use (models:- tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large):

`whisper audio.mp3 --model tiny`

- Specify which language the audio file is to reduce time:

`whisper audio.mp3 --language english`

- Specify where to save the converted files:

`whisper audio.mp3 --output_dir "./output"`

- Change the verbose settings of whisper:

`whisper audio.mp3 --verbose False`

# whisper

> 오디오 파일을 `txt`, `vtt`, `srt`, `tsv`, `json`으로 변환.
> 더 많은 정보: <https://github.com/openai/whisper>.

- 특정 오디오 파일을 모든 제공된 파일 형식으로 변환:

`whisper {{경로/대상/오디오.mp3}}`

- 변환된 파일의 출력 형식을 지정하여 오디오 파일 변환:

`whisper {{경로/대상/오디오.mp3}} --output_format {{txt}}`

- 특정 모델을 사용하여 오디오 파일 변환:

`whisper {{경로/대상/오디오.mp3}} --model {{tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}}`

- 오디오 파일의 언어를 지정하여 변환 시간을 단축하며 오디오 파일 변환:

`whisper {{경로/대상/오디오.mp3}} --language {{english}}`

- 오디오 파일을 변환하고 특정 위치에 저장:

`whisper {{경로/대상/오디오.mp3}} --output_dir "{{경로/대상/출력}}"`

- 조용한 모드로 오디오 파일 변환:

`whisper {{경로/대상/오디오.mp3}} --verbose {{False}}`

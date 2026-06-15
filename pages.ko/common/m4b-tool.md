# m4b-tool

> 챕터가 포함된 오디오북 파일을 병합, 분할 및 조작하는 도구.
> 더 많은 정보: <https://github.com/sandreas/m4b-tool>.

- 입력 디렉터리의 오디오 파일들로 오디오북 생성:

`m4b-tool merge {{경로/대상/입력_디렉터리}} {{[-o|--output-file]}}={{경로/대상/합쳐진_파일.m4b}}`

- 입력 파일 이름을 챕터 이름으로 사용하여 오디오북 생성:

`m4b-tool merge {{경로/대상/입력_디렉터리}} {{[-o|--output-file]}}={{경로/대상/합쳐진_파일.m4b}} --use-filenames-as-chapters`

- 오디오북을 챕터별 개별 파일로 분할:

`m4b-tool split {{경로/대상/오디오북.m4b}} {{[-o|--output-dir]}}={{경로/대상/출력_디렉터리}}`

- 오디오북을 MP3 파일들로 분할:

`m4b-tool split {{경로/대상/오디오북.m4b}} --audio-format {{mp3}} {{[-o|--output-dir]}}={{경로/대상/출력_디렉터리}}`

- 무음 구간을 이용하여 챕터 위치 조정:

`m4b-tool chapters {{경로/대상/오디오북.m4b}} --adjust-by-silence`

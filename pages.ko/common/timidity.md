# timidity

> MIDI 파일을 재생하고 변환합니다.
> 더 많은 정보: <https://manned.org/timidity>.

- MIDI 파일 재생:

`timidity {{경로/대상/파일.mid}}`

- MIDI 파일을 반복 재생:

`timidity --loop {{경로/대상/파일.mid}}`

- 특정 조로 MIDI 파일 재생 (0 = 다장조/가단조, -1 = 바장조/라단조, +1 = 사장조/마단조 등):

`timidity --force-keysig={{-플랫|+샤프}} {{경로/대상/파일.mid}}`

- MIDI 파일을 PCM (WAV) 오디오로 변환:

`timidity --output-mode={{w}} --output-file={{경로/대상/파일.wav}} {{경로/대상/파일.mid}}`

- MIDI 파일을 FLAC 오디오로 변환:

`timidity --output-mode={{F}} --output-file={{경로/대상/파일.flac}} {{경로/대상/파일.mid}}`

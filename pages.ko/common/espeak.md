# espeak

> 텍스트 음성 변환을 사용하여, 기본 사운드 장치를 통해 이야기.
> 더 많은 정보: <https://manned.org/espeak>.

- 문구를 큰 소리로 이야기:

`espeak "I like to ride my bike."`

- 파일을 소리내어 말하기:

`espeak -f {{경로/대상/파일}}`

- 출력을 직접 말하지 않고, WAV 오디오 파일로 저장:

`espeak -w {{파일이름.wav}} "It's GNU plus Linux"`

- 다른 목소리를 사용:

`espeak -v {{음성}}`

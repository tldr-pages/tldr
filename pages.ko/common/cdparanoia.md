# cdparanoia

> CD에서 오디오 트랙을 추출.
> 더 많은 정보: <https://xiph.org/paranoia/manual.html>.

- 모든 트랙을 추출해 `track#.wav`라는 이름의 개별 WAV 파일로 저장:

`cdparanoia {{[-B|--batch]}}`

- CD의 목차를 터미널에 표시:

`cdparanoia {{[-Q|--query]}}`

- 트랙 2부터 5까지를 추출해 하나의 WAV 파일로 저장:

`cdparanoia 2-5`

- 트랙 3을 추출하여 `경로/대상/파일.wav`라는 파일로 저장:

`cdparanoia 3 '{{경로/대상/파일.wav}}'`

# flac

> FLAC 파일을 인코딩, 디코딩 및 테스트.
> 더 많은 정보: <https://xiph.org/flac>.

- WAV 파일을 FLAC로 인코딩 (WAV 파일과 동일한 FLAC 파일이 생성됨):

`flac {{경로/대상/파일.wav}}`

- 출력 파일을 지정하여 WAV 파일을 FLAC로 인코딩:

`flac {{[-o|--output-name]}} {{경로/대상/출력파일.flac}} {{경로/대상/파일.wav}}`

- 출력 파일을 지정하여 FLAC 파일을 WAV로 인코딩:

`flac {{[-d|--decode]}} {{[-o|--output-name]}} {{경로/대상/출력파일.wav}} {{경로/대상/파일.flac}}`

- 올바른 인코딩을 위해 FLAC 파일을 테스트:

`flac {{[-t|--test]}} {{경로/대상/파일.flac}}`

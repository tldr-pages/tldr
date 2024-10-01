# chafa

> 터미널에서 이미지 출력.
> 참고: `catimg`, `pixterm`.
> 더 많은 정보: <https://hpjansson.org/chafa/man>.

- 터미널에서 직접 이미지를 렌더링:

`chafa {{경로/대상/파일}}`

- 24비트 색깔([c]olor) 이미지 렌더링:

`chafa -c full {{경로/대상/파일}}`

- 디더링을 사용하여 작은 색상 팔레트로 이미지 렌더링을 개선:

`chafa -c 16 --dither ordered {{경로/대상/파일}}`

- 이미지를 렌더링하여, 픽셀화된 것처럼 보이게 만듬:

`chafa --symbols vhalf {{경로/대상/파일}}`

- 점자 문자만 사용하여 흑백 이미지를 렌더링:

`chafa -c none --symbols braille {{경로/대상/파일}}`

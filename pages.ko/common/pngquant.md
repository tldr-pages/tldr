# pngquant

> PNG 변환기 및 손실 이미지 압축기.
> 더 많은 정보: <https://pngquant.org/>.

- 특정 PNG를 최대한 압축하고 결과를 새 파일에 저장:

`pngquant {{경로/대상/파일.png}}`

- 특정 PNG를 압축하고 원본 덮어쓰기:

`pngquant --ext .png --force {{경로/대상/파일.png}}`

- 사용자 지정 품질로 특정 PNG를 압축 시도 (최소값 미만인 경우 건너뜀):

`pngquant --quality {{0-100}} {{경로/대상/파일.png}}`

- 색상을 64개로 줄여 특정 PNG 압축:

`pngquant {{64}} {{경로/대상/파일.png}}`

- 압축 후 파일 크기가 원본보다 큰 경우 건너뛰기:

`pngquant --skip-if-larger {{경로/대상/파일.png}}`

- 메타데이터 제거 후 특정 PNG 압축:

`pngquant --strip {{경로/대상/파일.png}}`

- 특정 PNG를 압축하여 지정된 경로에 저장:

`pngquant {{경로/대상/파일.png}} --output {{경로/대상/파일.png}}`

- 진행 상황을 표시하며 특정 PNG 압축:

`pngquant --verbose {{경로/대상/파일.png}}`

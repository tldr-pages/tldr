# pngcrush

> PNG 압축 유틸리티.
> 더 많은 정보: <https://pmt.sourceforge.io/pngcrush>.

- PNG 파일 압축:

`pngcrush {{입력.png}} {{출력.png}}`

- 모든 PNG 파일 압축 후 지정된 디렉토리에 출력:

`pngcrush -d {{경로/대상/출력}} *.png`

- 사용 가능한 모든 114개의 알고리즘으로 PNG 파일을 압축하고 최상의 결과 선택:

`pngcrush -rem allb -brute -reduce {{입력.png}} {{출력.png}}`

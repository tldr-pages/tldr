# shuf

> 무작위 순열 생성.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- 파일의 줄 순서를 무작위로 변환하여 결과 출력:

`shuf {{경로/대상/파일}}`

- 결과의 처음 5개 항목만 출력:

`shuf --head-count=5 {{경로/대상/파일}}`

- 출력을 다른 파일에 쓰기:

`shuf {{경로/대상/입력_파일}} --output={{경로/대상/출력_파일}}`

- 1에서 10까지의 범위에서 무작위 숫자 생성:

`shuf --input-range=1-10`

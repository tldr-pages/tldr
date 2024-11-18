# yaa

> YAA 아카이브 생성 및 조작.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- 디렉터리에서 아카이브 생성:

`yaa archive -d {{경로/대상/폴더}} -o {{경로/대상/출력_파일.yaa}}`

- 파일에서 아카이브 생성:

`yaa archive -i {{경로/대상/파일}} -o {{경로/대상/출력_파일.yaa}}`

- 현재 디렉터리에 아카이브 추출:

`yaa extract -i {{경로/대상/아카이브_파일.yaa}}`

- 아카이브 내용 나열:

`yaa list -i {{경로/대상/아카이브_파일.yaa}}`

- 특정 압축 알고리즘으로 아카이브 생성:

`yaa archive -a {{알고리즘}} -d {{경로/대상/폴더}} -o {{경로/대상/출력_파일.yaa}}`

- 8 MB 블록 크기로 아카이브 생성:

`yaa archive -b 8m -d {{경로/대상/폴더}} -o {{경로/대상/출력_파일.yaa}}`

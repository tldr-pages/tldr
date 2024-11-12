# zipnote

> Zip 압축 파일의 주석을 보고, 추가하거나 편집.
> Zip 압축 파일에서 파일 이름도 변경 가능.
> 더 많은 정보: <https://manned.org/zipnote>.

- Zip 압축 파일의 주석 보기:

`zipnote {{경로/대상/파일.zip}}`

- Zip 압축 파일의 주석을 파일로 추출:

`zipnote {{경로/대상/파일.zip}} > {{경로/대상/파일.txt}}`

- 파일에서 주석을 추가/업데이트하여 Zip 압축 파일에 반영:

`zipnote -w {{경로/대상/파일.zip}} < {{경로/대상/파일.txt}}`

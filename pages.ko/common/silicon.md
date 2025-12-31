# silicon

> 소스 코드의 이미지를 생성.
> 더 많은 정보: <https://github.com/Aloxaf/silicon#examples>.

- 특정 소스 파일에서 이미지 생성:

`silicon {{경로/대상/소스_파일}} --output {{경로/대상/출력_이미지}}`

- 특정 프로그래밍 언어 구문 강조를 사용하여 소스 파일에서 이미지 생성 (예: `rust`, `py`, `js` 등):

`silicon {{경로/대상/소스_파일}} --output {{경로/대상/출력_이미지}} --language {{언어|확장자}}`

- `stdin`에서 이미지 생성:

`{{명령어}} | silicon --output {{경로/대상/출력_이미지}}`

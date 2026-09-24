# bluebuild

> `recipe.yml` 기반으로 Containerfile 및 커스텀 이미지 빌드.
> 더 많은 정보: <https://github.com/blue-build/cli#how-to-use>.

- 레시피 빌드:

`bluebuild build {{경로/대상/레시피.yml}}`

- 레시피 유효성 검사:

`bluebuild validate {{경로/대상/레시피.yml}}`

- 레시피로부터 Containerfile 생성:

`bluebuild generate {{[-o|--output]}} {{Containerfile}} {{경로/대상/레시피.yml}}`

- 레시피로부터 ISO 생성:

`bluebuild generate-iso --output-dir {{경로/대상/출력_디렉터리}} --iso-name {{iso_name.iso}} recipe {{경로/대상/레시피.yml}}`

- 도움말 표시:

`bluebuild {{[-h|--help]}}`

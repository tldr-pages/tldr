# czkawka-cli

> 중복 항목, 빈 폴더, 유사한 이미지 등을 찾는 다양한 기능의 앱 `czkawka`의 명령어 입력 버전.
> 더 많은 정보: <https://github.com/qarmin/czkawka>.

- 특정 디렉토리에 중복되거나 유사한 파일을 나열:

`czkawka-cli {{dup|image}} --directories {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`

- 특정 디렉터리에서 중복 파일을 찾아 삭제 (기본값: `NONE`):

`czkawka-cli dup --directories {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}} --delete-method {{AEN|AEO|ON|OO|HARD|NONE}}`

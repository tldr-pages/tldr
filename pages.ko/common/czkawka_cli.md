# czkawka_cli

> 중복 파일, 빈 폴더, 유사한 이미지 등을 찾음.
> 더 많은 정보: <https://github.com/qarmin/czkawka/blob/master/czkawka_cli/README.md>.

- 특정 디렉터리에서 중복 파일을 찾아 결과를 파일에 저장:

`czkawka_cli dup {{[-d|--directories]}} {{경로/대상/디렉터리1}} {{[-d|--directories]}} {{경로/대상/디렉터리2}} {{[-f|--file-to-save]}} {{경로/대상/결과파일.txt}}`

- 특정 디렉터리에서 중복 파일을 찾고 삭제 (기본값: `NONE`):

`czkawka_cli dup {{[-d|--directories]}} {{경로/대상/디렉터리}} {{[-D|--delete-method]}} {{AEN|AEO|ON|OO|HARD|NONE}}`

- 지정한 유사도 수준을 기준으로 유사한 이미지를 찾음 (기본값: `High`):

`czkawka_cli image {{[-d|--directories]}} {{경로/대상/디렉터리}} {{[-s|--similarity-preset]}} {{Minimal|VerySmall|Small|Medium|High|VeryHigh|Original}} {{[-f|--file-to-save]}} {{경로/대상/결과파일.txt}}`

- 도움말 표시:

`czkawka_cli {{[-h|--help]}}`

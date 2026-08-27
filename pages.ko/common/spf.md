# spf

> 최신 터미널 파일 관리자인 superfile.
> 더 많은 정보: <https://github.com/yorukot/superfile>.

- 지정한 경로에서 `spf` 실행:

`spf {{경로/대상/디렉터리}}`

- 여러 경로를 지정하여 `spf` 실행:

`spf {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`

- 누락된 단축키를 추가해 단축키 설정 수정:

`spf {{[--fh|--fix-hotkeys]}}`

- 누락된 항목을 추가해 설정 파일 수정:

`spf {{[--fch|--fix-config-file]}}`

- 지정한 설정 파일과 단축키 파일 수정:

`spf {{[-c|--config-file]}} {{경로/대상/설정파일.toml}} {{[--hf|--hotkey-file]}} {{경로/대상/단축키.toml}}`

- 처음 선택한 파일의 경로를 지정한 파일에 기록한 후 종료:

`spf {{[--cf|--chooser-file]}} {{tmp/지정한_파일경로}}`

- 내부 설정 및 데이터 디렉터리 경로 표시:

`spf {{[pl|path-list]}}`

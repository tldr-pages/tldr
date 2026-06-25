# ghcid

> 파일 변경 시 코드를 자동 리로드하는 간단하고 효율적인 Haskell CLI IDE.
> 컴파일 오류, 경고 및 테스트 결과를 지속적으로 표시.
> 더 많은 정보: <https://github.com/ndmitchell/ghcid>.

- `ghcid` 시작하고 Haskell 파일 변경 감시:

`ghcid {{경로/대상/Main.hs}}`

- Stack 또는 Cabal 프로젝트 로드 같은 특정 명령으로 `ghcid` 시작:

`ghcid --command "{{stack ghci Main.hs}}"`

- 파일 저장 시마다 특정 액션(기본값: `main`) 실행:

`ghcid --run={{action}} {{경로/대상/Main.hs}}`

- 최대 높이와 너비 설정 (기본값은 현재 콘솔 크기):

`ghcid --height={{높이}} --width={{너비}} {{경로/대상/Main.hs}}`

- 전체 GHC 컴파일러 출력을 파일로 저장:

`ghcid --outputfile={{경로/대상/output_file.txt}} {{경로/대상/Main.hs}}`

- 파일 저장 시마다 REPL 명령 실행 허용 (예: `-- $> 1+1`):

`ghcid --allow-eval {{경로/대상/Main.hs}}`

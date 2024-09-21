# brittany

> Haskell 소스 파일을 형식에 맞추어 출력.
> 더 많은 정보: <https://github.com/lspitzner/brittany#readme>.

- Haskell 소스 파일의 형식을 지정하고 결과를 `stdout`으로 인쇄:

`brittany {{경로/대상/file.hs}}`

- 현재 디렉터리에 있는 모든 Haskell 소스 파일을 바로 포맷:

`brittany --write-mode=inplace {{*.hs}}`

- Haskell 소스 파일에 변경이 필요한지 확인하고 프로그램 종료 코드를 통해 결과를 표시:

`brittany --check-mode {{경로/대상/file.hs}}`

- 들여쓰기 수준, 줄 길이 별로 지정된 공백 설정을 사용하여 Haskell 소스 파일 형식을 지정:

`brittany --indent {{4}} --columns {{100}} {{경로/대상/file.hs}}`

- 지정된 구성 파일에 정의된 스타일에 따라 Haskell 소스 파일의 형식을 지정:

`brittany --config-file {{경로/대상/config.yaml}} {{경로/대상/file.hs}}`

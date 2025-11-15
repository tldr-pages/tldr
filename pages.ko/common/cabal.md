# cabal

> Haskell 패키지 인프라 (Cabal)에 대한 명령어 라인 인터페이스.
> Hackage 패키지 저장소에서 Haskell 프로젝트 및 Cabal패키지 관리.
> 더 많은 정보: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

- Hackage에서 패키지 검색 및 리스트:

`cabal list {{검색할_문자열}}`

- 패키지에 대한 정보 출력:

`cabal info {{패키지_이름}}`

- 패키지 다운로드 및 설치:

`cabal install {{패키지_이름}}`

- 현재 디렉토리에서 새로운 Haskell 프로젝트 생성:

`cabal init`

- 현재 디렉토리에서 프로젝트 빌드:

`cabal build`

- 현재 디렉토리에서 프로젝트의 테스트 실행:

`cabal test`

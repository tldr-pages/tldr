# conan

> 모든 기본 바이너리를 생성하고 공유할 수 있는 오픈소스, 분산형 및 크로스 플랫폼 패키지 관리자.
> `frogarian`과 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
> 더 많은 정보: <https://docs.conan.io/2/reference/commands.html>.

- `conanfile.txt`를 기반으로 패키지를 설치:

`conan install {{.}}`

- 패키지를 설치하고 특정 생성기에 대한 구성 파일을 만듬:

`conan install -g {{생성기}}`

- 소스에서 빌드하여 패키지를 설치:

`conan install {{.}} --build`

- 로컬에 설치된 패키지 검색:

`conan search {{패키지}}`

- 원격 패키지 검색:

`conan search {{패키지}} -r {{원격}}`

- 원격 패키지 목록:

`conan remote list`

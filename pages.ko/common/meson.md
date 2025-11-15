# meson

> SCons와 유사한 빌드 시스템으로, Python을 프론트엔드 언어로 사용하고 Ninja를 빌드 백엔드로 사용합니다.
> 더 많은 정보: <https://mesonbuild.com/Commands.html>.

- 주어진 이름과 버전으로 C 프로젝트 생성:

`meson init --language={{c}} --name={{내프로젝트}} --version={{0.1}}`

- 기본값으로 `builddir` 구성:

`meson setup {{빌드_폴더}}`

- 프로젝트 빌드:

`meson compile -C {{경로/대상/빌드_폴더}}`

- 프로젝트의 모든 테스트 실행:

`meson test`

- 도움말 표시:

`meson --help`

- 버전 표시:

`meson --version`

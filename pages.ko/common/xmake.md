# xmake

> Lua 기반의 크로스 플랫폼 C & C++ 빌드 유틸리티.
> 더 많은 정보: <https://xmake.io/#/getting_started>.

- Hello World와 `xmake.lua`를 포함한 Xmake C 프로젝트 생성:

`xmake create {{[-l|--language]}} {{[c|clean]}} {{[-P|--project]}} {{프로젝트_이름}}`

- Xmake 프로젝트 빌드 및 실행:

`xmake {{[b|build]}} {{[r|run]}}`

- 컴파일된 Xmake 타겟을 직접 실행:

`xmake {{[r|run]}} {{타겟_이름}}`

- 프로젝트의 빌드 타겟 구성:

`xmake {{[f|config]}} {{[-p |--plat=]}}{{macosx|linux|iphoneos|...}} {{[-a |--arch=]}}{{x86_64|i386|arm64|...}} {{[-m |--mode=]}}{{debug|release}}`

- 컴파일된 타겟을 디렉토리에 설치:

`xmake {{[i|install]}} {{[-o |--installdir=]}}{{경로/대상/폴더}}`

# xcode-select

> Xcode의 다양한 버전과 포함된 개발자 도구 간에 전환.
> 설치 후 Xcode가 이동된 경우 경로를 업데이트하는 데 사용됩니다.
> 더 많은 정보: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Xcode의 명령줄 도구 설치:

`xcode-select --install`

- 주어진 경로를 활성 개발자 디렉토리로 선택:

`xcode-select --switch {{경로/대상/Xcode.app/Contents/Developer}}`

- 주어진 Xcode 인스턴스를 선택하고 해당 개발자 디렉토리를 활성 디렉토리로 사용:

`xcode-select --switch {{경로/대상/Xcode_파일.app}}`

- 현재 선택된 개발자 디렉토리 출력:

`xcode-select --print-path`

- 사용자 지정 개발자 디렉토리를 삭제하여 기본 검색 메커니즘을 통해 찾도록 설정:

`sudo xcode-select --reset`

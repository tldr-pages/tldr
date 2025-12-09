# codesign

> macOS용 코드 서명을 생성하고 조작합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- 애플리케이션을 인증서로 서명:

`codesign --sign "{{내 회사 이름}}" {{경로/대상/애플리케이션_파일.app}}`

- 애플리케이션의 인증서 검증:

`codesign --verify {{경로/대상/애플리케이션_파일.app}}`

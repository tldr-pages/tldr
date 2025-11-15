# open

> 파일, 디렉토리 및 애플리케이션을 엽니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/open.1.html>.

- 파일을 관련 애플리케이션으로 열기:

`open {{파일.ext}}`

- 그래픽 macOS [a]애플리케이션 실행:

`open -a "{{애플리케이션}}"`

- [b]번들 식별자를 기반으로 그래픽 macOS 앱 실행 (`osascript`를 사용하여 쉽게 얻을 수 있음):

`open -b {{com.domain.application}}`

- 현재 디렉토리를 Finder에서 열기:

`open .`

- 파일을 Finder에서 [R]표시:

`open -R {{경로/대상/파일}}`

- 현재 디렉토리에서 주어진 확장자의 모든 파일을 관련 애플리케이션으로 열기:

`open {{*.확장자}}`

- [b]번들 식별자를 통해 지정된 애플리케이션의 [n]새 인스턴스 열기:

`open -n -b {{com.domain.application}}`

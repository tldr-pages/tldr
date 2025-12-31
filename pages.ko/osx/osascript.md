# osascript

> AppleScript 또는 JavaScript for Automation (JXA) 실행.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- AppleScript 명령 실행:

`osascript -e '{{say "Hello world"}}'`

- 여러 AppleScript 명령 실행:

`osascript -e '{{say "Hello"}}' -e '{{say "world"}}'`

- 컴파일된(`*.scpt`), 번들(`*.scptd`), 또는 텍스트(`*.applescript`) 형식의 AppleScript 파일 실행:

`osascript {{경로/대상/apple.scpt}}`

- 애플리케이션의 번들 식별자 얻기 (`open -b`에 유용):

`osascript -e 'id of app "{{애플리케이션}}"'`

- JavaScript 명령 실행:

`osascript -l JavaScript -e "{{console.log('Hello world');}}"`

- JavaScript 파일 실행:

`osascript -l JavaScript {{경로/대상/script.js}}`

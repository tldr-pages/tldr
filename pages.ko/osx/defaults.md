# defaults

> macOS 사용자 애플리케이션 구성을 읽고 쓰기.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- 애플리케이션 옵션에 대한 시스템 기본값 읽기:

`defaults read "{{애플리케이션}}" "{{옵션}}"`

- 애플리케이션 옵션에 대한 기본값 읽기:

`defaults read -app "{{애플리케이션}}" "{{옵션}}"`

- 도메인 이름, 키 및 값에서 키워드 검색:

`defaults find "{{키워드}}"`

- 애플리케이션 옵션의 기본값 쓰기:

`defaults write "{{애플리케이션}}" "{{옵션}}" {{-타입}} {{값}}`

- Mission Control 애니메이션 속도 향상:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- 애플리케이션의 모든 기본값 삭제:

`defaults delete "{{애플리케이션}}"`

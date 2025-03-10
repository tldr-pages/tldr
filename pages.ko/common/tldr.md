# tldr

> tldr-pages 프로젝트에서 제공하는 명령줄 도구에 대한 간단한 도움말 페이지를 표시합니다.
> 참고: `--language` 및 `--list` 옵션은 클라이언트 사양에 필수는 아니지만 대부분의 클라이언트가 이를 구현합니다.
> 더 많은 정보: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- 특정 명령에 대한 tldr 페이지를 출력 (힌트: 이렇게 이곳에 도착했습니다!):

`tldr {{명령어}}`

- 특정 하위 명령에 대한 tldr 페이지를 출력:

`tldr {{명령어}} {{하위_명령어}}`

- 주어진 [L]언어로 된 명령어의 tldr 페이지를 출력 (가능한 경우, 그렇지 않으면 영어로 표시):

`tldr {{[-L|--language]}} {{언어_코드}} {{명령어}}`

- 특정 [p]플랫폼의 명령어에 대한 tldr 페이지를 출력:

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{명령어}}`

- tldr 페이지의 로컬 캐시 [u]업데이트:

`tldr {{[-u|--update]}}`

- 현재 플랫폼 및 `common`에 대한 모든 페이지 [l]목록:

`tldr {{[-l|--list]}}`

- 명령어에 대한 사용할 수 있는 모든 하위 명령 페이지 [l]목록:

`tldr {{[-l|--list]}} | grep {{명령어}} | column`

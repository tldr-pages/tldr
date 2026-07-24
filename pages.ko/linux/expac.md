# expac

> pacman 기반 유틸리티를 위해 printf와 유사한 형식 지정 기능을 제공하는 alpm 데이터베이스 정보 추출 도구.
> 관련 항목: `pacman`.
> 더 많은 정보: <https://github.com/falconindy/expac#name>.

- 패키지의 의존성 목록 표시:

`expac {{[-S|--sync]}} '%D' {{패키지}}`

- 패키지의 선택적 의존성 목록 표시:

`expac {{[-S|--sync]}} "%o" {{패키지}}`

- 패키지의 다운로드 크기를 MiB 단위로 표시:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' {{패키지1 패키지2 ...}}`

- 업그레이드 대상 패키지와 다운로드 크기 표시:

`expac {{[-S|--sync]}} {{[-H|--humansize]}} M '%k\t%n' $(pacman -Qqu) | sort {{[-sh|--sort --human-numeric-sort]}}`

- 명시적으로 설치한 패키지와 선택적 의존성 목록 표시:

`expac {{[-d|--delim]}} '\n\n' {{[-l|--listdelim]}} '\n\t' {{[-Q|--query]}} '%n\n\t%O' $(pacman -Qeq)`

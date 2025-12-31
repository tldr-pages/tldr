# nu

> Nushell("새로운 유형의 셸")은 명령줄에 대한 현대적이고 구조화된 접근 방식을 제공합니다.
> 같이 보기: `elvish`.
> 더 많은 정보: <https://www.nushell.sh/book/configuration.html#flag-behavior>.

- 대화형 셸 세션 시작:

`nu`

- 특정 명령 실행:

`nu --commands "{{echo 'nu is executed'}}"`

- 특정 스크립트 실행:

`nu {{경로/대상/스크립트.nu}}`

- 로깅을 포함하여 특정 스크립트 실행:

`nu --log-level {{error|warn|info|debug|trace}} {{경로/대상/스크립트.nu}}`

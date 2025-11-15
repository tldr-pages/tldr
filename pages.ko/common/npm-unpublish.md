# npm unpublish

> npm 레지스트리에서 패키지를 제거.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-unpublish>.

- 특정 패키지 버전 언퍼블리시:

`npm unpublish {{패키지_이름}}@{{버전}}`

- 전체 패키지 언퍼블리시:

`npm unpublish {{패키지_이름}} --force`

- 스코프가 있는 패키지 언퍼블리시:

`npm unpublish @{{스코프}}/{{패키지_이름}}`

- 언퍼블리시 전 타임아웃 기간 지정:

`npm unpublish {{패키지_이름}} --timeout {{밀리초_시간}}`

- 실수로 언퍼블리시하는 것을 방지하려면 `--dry-run` 플래그를 사용하여 무엇이 언퍼블리시될지를 확인:

`npm unpublish {{패키지_이름}} --dry-run`

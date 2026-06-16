# npm deprecate

> `npm` 패키지의 특정 버전 또는 버전 범위를 사용 중단 권장(deprecated) 상태로 표시하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-deprecate/>.

- 특정 버전을 deprecated로 표시:

`npm deprecate {{패키지_이름}}@{{버전}} "{{사용중단_메시지}}"`

- 특정 버전 범위를 deprecated로 표시:

`npm deprecate {{패키지_이름}}@"<{{버전_범위}}" "{{사용중단_메시지}}"`

- 특정 버전의 deprecated 상태 해제:

`npm deprecate {{패키지_이름}}@{{버전}} ""`

# npm explain

> 특정 패키지가 왜 설치되었는지, 의존성 관계와 포함 이유를 설명하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/explain/>.

- 특정 패키지가 설치된 이유 설명:

`npm {{[why|explain]}} {{패키지_이름}}`

- JSON 형식으로 설명 출력:

`npm {{[why|explain]}} {{패키지_이름}} --json`

- peer 의존성까지 포함하여 설명:

`npm {{[why|explain]}} {{패키지_이름}} --include peer`

- 설명 깊이를 2단계로 제한:

`npm {{[why|explain]}} {{패키지_이름}} --depth 2`

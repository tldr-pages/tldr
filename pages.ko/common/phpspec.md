# phpspec

> PHP용 행동 주도 개발 도구.
> 더 많은 정보: <https://phpspec.net>.

- 클래스에 대한 사양 작성:

`phpspec describe {{클래스_이름}}`

- "spec" 폴더의 모든 사양 실행:

`phpspec run`

- 단일 사양 실행:

`phpspec run {{경로/대상/클래스_사양_파일}}`

- 특정 구성 파일을 사용하여 사양 실행:

`phpspec run -c {{경로/대상/구성_파일}}`

- 특정 부트스트랩 파일을 사용하여 사양 실행:

`phpspec run -b {{경로/대상/부트스트랩_파일}}`

- 코드 생성 프롬프트 비활성화:

`phpspec run --no-code-generation`

- 가짜 반환 값 활성화:

`phpspec run --fake`

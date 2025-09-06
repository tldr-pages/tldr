# kahlan

> PHP용 단위 테스트 및 행동 주도 개발 테스트 프레임워크.
> 더 많은 정보: <https://kahlan.github.io/docs/cli-options.html>.

- "spec" 디렉토리의 모든 사양 실행:

`kahlan`

- 특정 구성 파일을 사용하여 사양 실행:

`kahlan --config={{경로/대상/구성_파일}}`

- 리포터를 사용하여 사양 실행 및 출력:

`kahlan --reporter={{dot|bar|json|tap|verbose}}`

- 코드 커버리지와 함께 사양 실행 (세부 수준은 0에서 4 사이):

`kahlan --coverage={{세부_수준}}`

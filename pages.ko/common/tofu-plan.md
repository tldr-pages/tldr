# tofu plan

> OpenTofu 실행 계획을 생성하고 표시.
> 더 많은 정보: <https://opentofu.org/docs/cli/commands/plan/>.

- 현재 디렉터리에서 실행 계획 생성 및 표시:

`tofu plan`

- 현재 존재하는 모든 원격 객체를 삭제하기 위한 실행 계획 표시:

`tofu plan -destroy`

- Tofu 상태와 출력값만 업데이트하기 위한 실행 계획 표시:

`tofu plan -refresh-only`

- 입력 변수 값 지정:

`tofu plan -var '{{이름1}}={{값1}}' -var '{{이름2}}={{값2}}'`

- 지정한 일부 리소스만 대상으로 Tofu 실행 계획 생성:

`tofu plan -target {{리소스_타입.리소스_이름[인스턴스_인덱스]}}`

- 실행 계획을 JSON 형식으로 출력:

`tofu plan -json`

- 실행 계획을 색상 코드 없이 지정한 파일에 저장:

`tofu plan -no-color > {{path/to/file}}`

# tofu output

> OpenTofu 리소스에 대한 구조화된 출력 데이터를 내보냄.
> 더 많은 정보: <https://opentofu.org/docs/cli/commands/output/>.

- 루트 모듈의 모든 출력값 표시:

`tofu output`

- 지정한 이름의 출력값만 표시:

`tofu output {{이름}}`

- 출력값을 원시 문자열로 출력 (쉘 스크립트에서 유용):

`tofu output -raw`

- 각 출력값을 키로 가지는, JSON 객체 형식으로 출력 (`jq`와 함께 사용하기에 유용):

`tofu output -json`

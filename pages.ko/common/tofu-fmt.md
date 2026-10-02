# tofu fmt

> OpenTofu 언어 스타일 규칙에 따라 설정 파일을 포맷.
> 더 많은 정보: <https://opentofu.org/docs/cli/commands/fmt/>.

- 현재 디렉터리의 설정 파일 포맷:

`tofu fmt`

- 현재 디렉터리와 모든 하위 디렉터리의 설정 파일 포맷:

`tofu fmt -recursive`

- 포맷으로 변경되는 내용의 diff 표시:

`tofu fmt -diff`

- 포맷된 파일 목록을 `stdout`에 출력하지 않음:

`tofu fmt -list=false`

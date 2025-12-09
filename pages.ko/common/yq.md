# yq

> 가볍고 휴대 가능한 명령줄 YAML 프로세서.
> 더 많은 정보: <https://mikefarah.gitbook.io/yq/>.

- YAML 파일을 보기 좋게 출력 (v4+):

`yq eval {{경로/대상/파일.yaml}}`

- YAML 파일을 보기 좋게 출력 (v3):

`yq read {{경로/대상/파일.yaml}} --colors`

- 배열만 포함된 YAML 파일에서 첫 번째 요소 출력 (v4+):

`yq eval '.[0]' {{경로/대상/파일.yaml}}`

- 배열만 포함된 YAML 파일에서 첫 번째 요소 출력 (v3):

`yq read {{경로/대상/파일.yaml}} '[0]'`

- 파일에서 키를 값으로 설정 (또는 덮어쓰기) (v4+):

`yq eval '.{{키}} = "{{값}}"' --inplace {{경로/대상/파일.yaml}}`

- 파일에서 키를 값으로 설정 (또는 덮어쓰기) (v3):

`yq write --inplace {{경로/대상/파일.yaml}} '{{키}}' '{{값}}'`

- 두 파일을 병합하여 `stdout`에 출력 (v4+):

`yq eval-all 'select(filename == "{{경로/대상/파일1.yaml}}") * select(filename == "{{경로/대상/파일2.yaml}}")' {{경로/대상/파일1.yaml}} {{경로/대상/파일2.yaml}}`

- 두 파일을 병합하여 `stdout`에 출력 (v3):

`yq merge {{경로/대상/파일1.yaml}} {{경로/대상/파일2.yaml}} --colors`

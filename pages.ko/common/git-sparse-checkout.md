# git sparse-checkout

> 저장소 전체가 아닌 일부 파일만 checkout 수행.
> 더 많은 정보: <https://manned.org/git-sparse-checkout>.

- sparse checkout 활성화:

`git sparse-checkout init`

- sparse checkout 비활성화 및 전체 저장소 복원:

`git sparse-checkout disable`

- 포함할 디렉터리(또는 파일) 지정:

`git sparse-checkout set {{경로/대상/디렉터리}}`

- 이후 추가 경로 포함하기:

`git sparse-checkout add {{경로/대상/디렉터리}}`

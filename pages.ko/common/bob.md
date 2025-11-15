# bob

> Neovim 버전을 관리하고 전환.
> 더 많은 정보: <https://github.com/MordechaiHadad/bob>.

- 지정된 버전의 Neovim을 설치하고 전환:

`bob use {{nightly|stable|latest|version_string|commit_hash}}`

- Neovim의 설치 및 현재 사용되는 버전을 출력:

`bob list`

- 특정 버전의 Neovim을 제거:

`bob uninstall {{nightly|stable|latest|version_string|commit_hash}}`

- Neovim을 제거하고 `bob`이 변경한 내용을 모두 삭제:

`bob erase`

- 이전에 최신으로 수정된 버전으로 롤백:

`bob rollback`

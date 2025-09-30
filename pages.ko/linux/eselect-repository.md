# eselect repository

> Portage를 위한 ebuild 저장소를 구성하는 `eselect` 모듈.
> 저장소를 활성화한 후에는 `emerge --sync repo_name`을 실행하여 ebuild를 다운로드해야 합니다.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- <https://repos.gentoo.org>에 등록된 모든 ebuild 저장소 나열:

`eselect repository list`

- 활성화된 저장소 나열:

`eselect repository list -i`

- `list` 명령에서 이름이나 색인으로 저장소 활성화:

`eselect repository enable {{이름|색인}}`

- 등록되지 않은 저장소 활성화:

`eselect repository add {{이름}} {{rsync|git|mercurial|svn|...}} {{동기화_URI}}`

- 저장소의 내용을 제거하지 않고 비활성화:

`eselect repository disable {{저장소1 저장소2 ...}}`

- 저장소를 비활성화하고 내용을 제거:

`eselect repository remove {{저장소1 저장소2 ...}}`

- 로컬 저장소를 생성하고 활성화:

`eselect repository create {{이름}} {{경로/대상/저장소}}`

# jj

> Jujutsu 버전 관리 시스템.
> `log`, `desc`, `new`, `git` 등 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/>.

- 지정한 revset의 revision 설명 업데이트 (예: `B::D`, `A..D`, `B|C|D` 등):

`jj {{[desc|describe]}} {{[-m|--message]}} "{{메시지}}" {{[-r|--revision]}} {{revsets}}`

- 지정한 리비전 위에 새로운 커밋/리비전 생성:

`jj new {{revset}}`

- 여러 리비전 위에 새로운 병합 커밋 생성:

`jj new {{revset1 revset2 ...}}`

- 작업 복사본을 지정한 리비전으로 이동:

`jj edit {{revset}}`

- 이전 명령 실행 취소 (`undo`도 포함):

`jj undo`

- 작업 복사본을 스냅샷하지 않고 jj 하위 명령 실행:

`jj --ignore-working-copy {{하위_명령어}}`

- 지정한 작업 시점에서 jj 하위 명령 실행:

`jj {{[--at-op|--at-operation]}} {{작업}} {{하위_명령어}}`

- 지정한 하위 명령의 도움말 표시 (`new`, `commit`, `desc` 등):

`jj help {{하위_명령어}}`

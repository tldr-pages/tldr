# jj absorb

> 소스 리비전의 변경 사항을 분리하여, 각 변경 사항을 해당 줄이 마지막으로 수정된 가장 가까운 수정이 가능한 조상 리비전으로 이동.
> 조상 리비전에서 일치하는 위치가 없거나 여러 개인 변경 사항은 이동되지 않음.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-absorb>.

- 지정한 리비전의 이동 가능한 모든 변경 사항을 다른 리비전으로 자동 이동:

`jj absorb {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revsets}}`

- 지정한 파일의 변경 사항만 다른 리비전으로 이동:

`jj absorb {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revsets}} {{filesets}}`

# chgrp

> 파일 및 디렉토리의 그룹 소유권 변경.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- 파일/디렉토리의 소유 그룹 변경:

`chgrp {{그룹}} {{경로/파일명_또는_디렉토리명}}`

- 디렉토리 및 해당 컨텐츠의 소유 그룹 변경:

`chgrp {{[-R|--recursive]}} {{그룹}} {{경로/디렉토리명}}`

- 심볼릭 링크의 소유 그룹 변경:

`chgrp {{[-h|--no-dereference]}} {{그룹}} {{경로/심볼릭_링크}}`

- 참조 파일과 일치하도록 파일/디렉토리의 소유 그룹 변경:

`chgrp --reference {{경로/참조_파일명}} {{경로/파일명_또는_디렉토리명}}`

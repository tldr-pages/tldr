# bmaptool

> 블록 맵을 지능적으로 생성 및 복사( `cp` 혹은 `dd`보다 빠른 속도).
> 더 많은 정보: <https://manned.org/bmaptool>.

- 이미지 파일에서 블록 맵 생성:

`bmaptool create -o {{블록맵.bmap}} {{이미지 파일}}`

- 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap {{블록맵.bmap}} {{이미지 파일}} {{/dev/sdb}}`

- 압축된 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap {{블록맵.bmap}} {{압축된 이미지 파일}} {{/dev/sdb}}`

- 블록맵을 사용하지 않고 이미지 파일을 sdb로 복사:

`bmaptool copy --nobmap {{이미지 파일}} {{/dev/sdb}}`

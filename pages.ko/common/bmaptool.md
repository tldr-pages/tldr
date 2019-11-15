# bmaptool

> 블록 맵을 지능적으로 생성 및 복사( `cp` 혹은 `dd`보다 빠른 속도).
> More information: <https://source.tizen.org/documentation/reference/bmaptool>.

- 이미지 파일에서 블록 맵 생성:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- 압축된 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- 블록맵을 사용하지 않고 이미지 파일을 sdb로 복사:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`

# bmaptool

> 大文件，比如raw镜像文件，相对传统工具‘dd’或者‘cp’，使用bmaptool可以更可靠.
> 详见: <https://source.tizen.org/zh-hans/documentation/reference/bmaptool?langswitch=zh-hans>.

- 使用图片生成块图文件:

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- 复制图片到指定目录:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- 复制压缩后的图片到指定目录:

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- 复制图片的时候，不将图片转成块图:

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`

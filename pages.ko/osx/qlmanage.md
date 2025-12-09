# qlmanage

> QuickLook 서버 도구.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- 하나 또는 여러 [f]파일에 대해 QuickLook 표시:

`qlmanage -p {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 현재 폴더의 모든 JPEG 파일에 대해 300px 너비의 PNG 썸네일 생성 후, 지정된 폴더에 저장:

`qlmanage {{*.jpg}} -t -s {{300}} {{경로/대상/폴더}}`

- QuickLook 재설정:

`qlmanage -r`

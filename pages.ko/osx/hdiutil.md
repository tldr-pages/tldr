# hdiutil

> 디스크 이미지를 생성하고 관리하는 유틸리티.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- 이미지를 마운트:

`hdiutil attach {{경로/대상/이미지_파일}}`

- 이미지를 마운트 해제:

`hdiutil detach /Volumes/{{볼륨_파일}}`

- 마운트된 이미지 목록 표시:

`hdiutil info`

- 디렉터리의 내용을 ISO 이미지로 생성:

`hdiutil makehybrid -o {{경로/대상/출력_파일}} {{경로/대상/폴더}}`

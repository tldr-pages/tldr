# unsquashfs

> squashfs 파일 시스템의 압축을 풀고, 파일을 추출하거나 나열합니다.
> 더 많은 정보: <https://manned.org/unsquashfs>.

- squashfs 파일 시스템을 현재 작업 디렉토리의 `squashfs-root`에 추출:

`unsquashfs {{파일_시스템.squashfs}}`

- squashfs 파일 시스템을 지정된 디렉토리에 추출:

`unsquashfs -dest {{경로/대상/폴더}} {{파일_시스템.squashfs}}`

- 파일이 추출될 때 파일 이름 표시:

`unsquashfs -info {{파일_시스템.squashfs}}`

- 파일이 추출될 때 파일 이름과 속성 표시:

`unsquashfs -linfo {{파일_시스템.squashfs}}`

- squashfs 파일 시스템 내부의 파일 나열 (추출하지 않고):

`unsquashfs -ls {{파일_시스템.squashfs}}`

- squashfs 파일 시스템 내부의 파일과 속성 나열 (추출하지 않고):

`unsquashfs -lls {{파일_시스템.squashfs}}`

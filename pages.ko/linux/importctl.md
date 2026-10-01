# importctl

> 디스크 이미지를 다운로드, 가져오기 또는 내보내기.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/importctl.html>.

- url에서 tarball 형식의 이미지를 다운로드:

`sudo importctl pull-tar {{url}} {{경로/대상/디렉터리}}`

- 원격의 raw 또는 `.qcow2` 파일 이미지를 다운로드하여 raw 파일로 저장:

`sudo importctl pull-raw {{https://example.com/source.ext}} {{이름}} --class={{machine|portable|sysext|confext}}`

- raw 디스크 이미지를 이미지 디렉터리로 가져오기 (`xz`, `gzip`, `bzip2` 압축 지원):

`importctl import-raw {{경로/대상/파일.ext}} {{이름}} --class={{machine|portable|sysext|confext}}`

- 컨테이너 이미지를 tarball 형식으로 현재 작업 디렉터리에 내보내기:

`importctl export-tar --class={{machine|portable|sysext|confext}} {{이름}} {{경로/대상/파일.ext}}`

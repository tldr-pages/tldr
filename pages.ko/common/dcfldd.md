# dcfldd

> 법의학 및 보안을 위한 향상된 dd 버전.
> 더 많은 정보: <https://manned.org/dcfldd>.

- 원시 이미지 파일에 디스크를 복사하고 SHA256을 사용해 이미지를 해시:

`dcfldd if={{/dev/disk_device}} of={{파일.img}} hash=sha256 hashlog={{파일.hash}}`

- 디스크를 원시 이미지 파일에 복사하여, 각 1GB 청크를 해싱:

`dcfldd if={{/dev/disk_device}} of={{파일.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{파일.hash}} hashwindow={{1G}}`

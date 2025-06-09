# mknod

> 블록 또는 문자 장치 특수 파일 생성.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- 블록 장치 생성:

`sudo mknod {{경로/대상/장치_파일}} b {{주_장치_번호}} {{부_장치_번호}}`

- 문자 장치 생성:

`sudo mknod {{경로/대상/장치_파일}} c {{주_장치_번호}} {{부_장치_번호}}`

- FIFO(큐) 장치 생성:

`sudo mknod {{경로/대상/장치_파일}} p`

- 기본 SELinux 보안 컨텍스트로 장치 파일 생성:

`sudo mknod {{[-Z |--context=]}}{{경로/대상/장치_파일}} {{유형}} {{주_장치_번호}} {{부_장치_번호}}`

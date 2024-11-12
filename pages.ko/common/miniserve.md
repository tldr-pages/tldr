# miniserve

> 간단한 HTTP 파일 서버.
> 더 많은 정보: <https://github.com/svenstaro/miniserve>.

- 디렉터리 서빙:

`miniserve {{경로/대상/폴더}}`

- 단일 파일 서빙:

`miniserve {{경로/대상/파일}}`

- HTTP 기본 인증을 사용하여 디렉터리 서빙:

`miniserve --auth {{사용자이름}}:{{비밀번호}} {{경로/대상/폴더}}`

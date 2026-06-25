# ots

> 한 번만 볼 수 있는 URL을 통해 종단 간 암호화된 비밀 정보를 공유하는 도구.
> 더 많은 정보: <https://github.com/sniptt-official/ots>.

- 새로운 비밀 생성:

`ots new`

- 만료 시간을 시간 단위로 지정해 비밀 생성 (기본값: 24):

`ots new -x {{시간_단위_숫자}}h`

- 비밀을 저장할 서버 지역 지정 (기본값: `us-east-1`):

`ots new --region {{지역_서버_아이디}}`

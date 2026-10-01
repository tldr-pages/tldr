# rpcdump.py

> Endpoint Mapper를 통해 원격 RPC 엔드포인트 정보를 출력.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 사용자명과 비밀번호를 사용해 RPC 엔드포인트 정보 출력:

`rpcdump.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- NTLM 해시를 사용해 RPC 엔드포인트 정보 출력:

`rpcdump.py -hashes {{LMHASH}}:{{NTHASH}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 대상 IP 주소를 직접 지정해 RPC 엔드포인트 정보 출력 (대상 이름이 NetBIOS 이름인 경우 유용):

`rpcdump.py -target-ip {{대상_아이피}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 특정 포트에 연결 (RPC Endpoint Mapper의 기본 포트는 135):

`rpcdump.py -port {{포트_번호}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 디버그 출력 활성화:

`rpcdump.py -debug {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

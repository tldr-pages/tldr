# rpcmap.py

> 문자열 바인딩(예: `ncacn_ip_tcp:host[port]`)을 사용하여 수신 대기 중인 MSRPC 인터페이스를 조회.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 문자열 바인딩을 사용하여 MSRPC 인터페이스에 연결 (예: `ncacn_ip_tcp:host[port]`):

`rpcmap.py {{문자열_바인딩}}`

- MGMT 인터페이스를 사용할 수 있는 경우에도 UUID 무차별 대입:

`rpcmap.py -brute-uuids {{문자열_바인딩}}`

- 검색된 UUID의 작업 번호(opnums) 무차별 대입:

`rpcmap.py -brute-opnums {{문자열_바인딩}}`

- 검색된 UUID의 메이저 버전 무차별 대입:

`rpcmap.py -brute-versions {{문자열_바인딩}}`

- 대상 IP 주소를 직접 지정:

`rpcmap.py -target-ip {{ip_주소}} {{문자열_바인딩}}`

- 사용자 이름과 비밀번호로 RPC 인터페이스 인증:

`rpcmap.py -auth-rpc {{도메인}}/{{사용자명}}:{{비밀번호}} {{문자열_바인딩}}`

- NTLM 해시를 사용해 RPC 인증:

`rpcmap.py -hashes-rpc {{LMHASH:NTHASH}} {{문자열_바인딩}}`

- Enable debug output for verbose information:

`rpcmap.py -debug {{문자열_바인딩}}`

# ssh-keyscan

> 원격 호스트의 공개 SSH 키를 가져옵니다.
> 더 많은 정보: <https://man.openbsd.org/ssh-keyscan>.

- 원격 호스트의 모든 공개 SSH 키 가져오기:

`ssh-keyscan {{호스트}}`

- 특정 포트에서 대기 중인 원격 호스트의 모든 공개 SSH 키 가져오기:

`ssh-keyscan -p {{포트}} {{호스트}}`

- 원격 호스트의 특정 유형의 공개 SSH 키 가져오기:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{호스트}}`

- 주어진 호스트의 지문으로 SSH known_hosts 파일 수동 업데이트:

`ssh-keyscan -H {{호스트}} >> ~/.ssh/known_hosts`

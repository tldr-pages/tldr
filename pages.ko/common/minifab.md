# minifab

> Hyperledger Fabric 네트워크의 설정 및 배포를 자동화.
> 더 많은 정보: <https://github.com/hyperledger-labs/minifabric>.

- 기본 Hyperledger Fabric 네트워크 시작:

`minifab up -i {{minifab_버전}}`

- Hyperledger Fabric 네트워크 중지:

`minifab down`

- 지정된 채널에 체인코드 설치:

`minifab install -n {{체인코드_이름}}`

- 특정 버전의 체인코드를 채널에 설치:

`minifab install -n {{체인코드_이름}} -v {{체인코드_버전}}`

- 설치/업그레이드 후 체인코드 초기화:

`minifab approve,commit,initialize,discover`

- 지정된 인수로 체인코드 메서드 호출:

`minifab invoke -n {{체인코드_이름}} -p '"{{메서드_이름}}", "{{인수1}}", "{{인수2}}", ...'`

- 원장에 쿼리 실행:

`minifab blockquery {{블록_번호}}`

- 애플리케이션을 빠르게 실행:

`minifab apprun -l {{앱_프로그래밍_언어}}`

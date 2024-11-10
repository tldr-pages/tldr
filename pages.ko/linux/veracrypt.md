# veracrypt

> 무료 및 오픈 소스 디스크 암호화 소프트웨어.
> 더 많은 정보: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- 텍스트 사용자 인터페이스를 통해 새 볼륨을 생성하고 `/dev/urandom`을 무작위 데이터의 소스로 사용:

`veracrypt --text --create --random-source={{/dev/urandom}}`

- 텍스트 사용자 인터페이스를 통해 볼륨을 상호작용적으로 복호화하고 디렉토리에 마운트:

`veracrypt --text {{경로/대상/볼륨}} {{경로/대상/마운트_포인트}}`

- 키 파일을 사용하여 파티션을 복호화하고 디렉토리에 마운트:

`veracrypt --keyfiles={{경로/대상/키파일}} {{/dev/sdXN}} {{경로/대상/마운트_포인트}}`

- 마운트된 디렉토리에서 볼륨 마운트 해제:

`veracrypt --dismount {{경로/대상/마운트된_포인트}}`

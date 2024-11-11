# solo

> Solo 하드웨어 보안 키와 상호 작용.
> 더 많은 정보: <https://github.com/solokeys/solo-python>.

- 연결된 Solo 목록 표시:

`solo ls`

- 현재 연결된 Solo의 펌웨어를 최신 버전으로 업데이트:

`solo key update`

- 특정 Solo의 LED 깜빡이기:

`solo key wink --serial {{일련_번호}}`

- 현재 연결된 Solo의 안전한 난수 생성기를 사용하여 무작위 바이트 생성:

`solo key rng raw`

- Solo의 직렬 출력 모니터링:

`solo monitor {{경로/대상/직렬_포트}}`

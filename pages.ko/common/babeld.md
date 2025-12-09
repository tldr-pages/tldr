# babeld

> 방화벽-스타일 필터를 사용하는 Babel용 라우팅 데몬입니다.
> 더 많은 정보: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- 하나 이상의 구성([c]onfiguration) 파일을 사용하여 데몬을 시작 (순서대로 읽음):

`babeld -c {{경로/대상/ports.conf}} -c {{경로/대상/filters.conf}} -c {{경로/대상/interfaces.conf}}`

- 시작 후 데몬화([D]eamonize):

`babeld -D`

- 구성([C]onfiguration) 명령어를 지정:

`babeld -C {{'redistribute metric 256'}}`

- 작동할 인터페이스를 지정:

`babeld {{eth0}} {{eth1}} {{wlan0}}`

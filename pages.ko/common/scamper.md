# scamper

> 인터넷을 능동적으로 탐색하여 토폴로지와 성능을 분석.
> `sc_`로 시작하는 몇 가지 도구를 포함, 예를 들어 `sc_warts2text` 또는 `sc_ttlexp`.
> 더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 목적지에 표준 옵션(트레이서트) 실행:

`scamper -i {{192.0.2.1}}`

- 두 가지 작업(핑 및 트레이서트)을 두 개의 다른 대상에 실행:

`scamper -I "{{ping}} {{192.0.2.1}}" -I "{{trace}} {{192.0.2.2}}"`

- 여러 호스트에 UDP로 핑, 첫 번째 핑에 특정 포트 번호를 사용하고 각 후속 핑마다 증가:

`scamper -c "{{ping}} -P {{UDP-목적지_포트}} -d {{33434}}" -i {{192.0.2.1}} -i {{192.0.2.2}}`

- 다중 경로 발견 알고리즘(MDA)을 사용하여 목적지로의 로드 밸런싱 경로 존재 여부를 결정하고 ICMP 에코 패킷을 사용하여 최대 세 번 시도하여 샘플링한 결과를 `warts` 파일에 기록:

`scamper -O {{warts}} -o {{경로/대상/출력.warts}} -I "{{tracelb}} -P {{ICMP-echo}} -q {{3}} {{192.0.2.1}}"`

- 목적지에 ICMP로 파리 트레이서트 실행하고 결과를 압축된 `warts` 파일에 저장:

`scamper -O {{warts.gz}} -o {{경로/대상/출력.warts}} -I "{{trace}} -P {{icmp-paris}} {{2001:db8:dead:beaf::4}}"`

- 특정 IP 주소에 도착하는 모든 ICMP 패킷과 특정 ICMP ID를 `warts` 파일에 기록:

`scamper -O {{warts}} -o {{경로/대상/출력.warts}} -I "sniff -S {{2001:db8:dead:beef::6}} icmp[icmpid] == {{101}}"`

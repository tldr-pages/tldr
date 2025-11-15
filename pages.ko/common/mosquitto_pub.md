# mosquitto_pub

> 단일 메시지를 주제에 게시하고 종료하는 간단한 MQTT 버전 3.1.1 클라이언트.
> 더 많은 정보: <https://mosquitto.org/man/mosquitto_pub-1.html>.

- Quality of Service(QoS)를 1로 설정하고, 192.168.1.1(기본값은 `localhost`)에 `sensors/temperature` 주제로 온도 값 32 게시:

`mosquitto_pub -h {{192.168.1.1}} -t {{sensors/temperature}} -m {{32}} -q {{1}}`

- 비표준 포트로 원격 호스트에 `sensors/temperature` 주제로 타임스탬프와 온도 데이터 게시:

`mosquitto_pub -h {{192.168.1.1}} -p {{1885}} -t {{sensors/temperature}} -m "{{1266193804 32}}"`

- 스위치 이벤트 사이에 긴 시간이 있을 수 있으므로, 원격 호스트에 `switches/kitchen_lights/status` 주제로 스위치 상태 게시 및 메시지 유지:

`mosquitto_pub -r -h "{{iot.eclipse.org}}" -t {{switches/kitchen_lights/status}} -m "{{on}}"`

- 파일(`data.txt`)의 내용을 메시지로 전송하고 `sensors/temperature` 주제로 게시:

`mosquitto_pub -t {{sensors/temperature}} -f {{data.txt}}`

- `stdin`에서 읽어들인 파일(`data.txt`)의 전체 입력 내용을 메시지로 전송하고 `sensors/temperature` 주제로 게시:

`mosquitto_pub -t {{sensors/temperature}} -s < {{data.txt}}`

- `stdin`에서 줄바꿈된 데이터를 메시지로 읽어들여 `sensors/temperature` 주제로 게시:

`{{echo data.txt}} | mosquitto_pub -t {{sensors/temperature}} -l`

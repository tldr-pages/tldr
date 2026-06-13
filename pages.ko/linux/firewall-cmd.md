# firewall-cmd

> firewalld 명령줄 클라이언트.
> 런타임 또는 영구 방화벽 구성 상태를 조회 및 수정.
> 더 많은 정보: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- 런타임 구성 상태에서 사용 가능한 모든 방화벽 영역과 규칙 조회:

`firewall-cmd --list-all-zones`

- 인터페이스를 block 영역으로 영구적으로 이동하여 모든 통신 차단:

`firewall-cmd --permanent --zone={{block}} --change-interface={{enp1s0}}`

- 지정된 영역에서 서비스의 포트를 영구적으로 열기 (예: `public` 영역에서 포트 443):

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- 지정된 영역에서 서비스의 포트를 영구적으로 닫기 (예: `public` 영역에서 포트 80):

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- 지정된 영역에서 들어오는 패킷의 포트를 영구적으로 포워딩 (예: `public` 영역에서 포트 443을 8443으로):

`firewall-cmd --permanent --zone={{public}} --add-rich-rule='rule family="{{ipv4|ipv6}}" forward-port port="{{443}}" protocol="{{udp|tcp}}" to-port="{{8443}}"'`

- firewalld를 다시 로드하여 런타임 변경 사항을 제거하고 영구 구성을 즉시 적용:

`firewall-cmd --reload`

- 런타임 구성 상태를 영구 구성으로 저장:

`firewall-cmd --runtime-to-permanent`

- 비상시 패닉 모드 활성화. 모든 트래픽이 차단되고 활성 연결이 종료됨:

`firewall-cmd --panic-on`

# route

> 수동으로 라우팅 테이블을 조작합니다.
> 관리자 권한이 필요합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/route.8.html>.

- 게이트웨이를 통해 대상지로의 경로 추가:

`sudo route add "{{대상_IP_주소}}" "{{게이트웨이_주소}}"`

- 게이트웨이를 통해 /24 서브넷으로의 경로 추가:

`sudo route add "{{서브넷_IP_주소}}/24" "{{게이트웨이_주소}}"`

- 테스트 모드로 실행(실행하지 않고 출력만 합니다):

`sudo route -t add "{{대상_IP_주소}}/24" "{{게이트웨이_주소}}"`

- 모든 경로 제거:

`sudo route flush`

- 특정 경로 삭제:

`sudo route delete "{{대상_IP_주소}}/24"`

- 대상지(호스트명 또는 IP 주소)의 경로 조회 및 표시:

`sudo route get "{{대상}}"`

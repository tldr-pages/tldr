# tailscale file

> Tailscale 네트워크에서 연결된 장치 간에 파일을 전송.
> 현재 동일한 Tailscale 네트워크 내에서도 다른 사용자가 소유한 장치로 파일을 보내는 것은 지원하지 않습니다.
> 더 많은 정보: <https://tailscale.com/kb/1106/taildrop/>.

- 특정 노드로 파일 전송:

`sudo tailscale file cp {{경로/대상/파일}} {{호스트명|IP}}:`

- 현재 노드로 전송된 파일을 특정 디렉토리에 저장:

`sudo tailscale file get {{경로/대상/폴더}}`

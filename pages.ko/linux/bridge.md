# bridge

> 네트워크 브릿지와 인터페이스를 조회 및 관리하는 도구.
> 더 많은 정보: <https://manned.org/bridge>.

- 모든 브릿지와 인터페이스 목록 출력:

`bridge {{[l|link]}}`

- 포트 VLAN 정보 출력:

`bridge {{[v|vlan]}}`

- VLAN 할당:

`sudo bridge {{[v|vlan]}} {{[a|add]}} dev {{lanX}} vid {{vlan_id}} pvid {{tagged|untagged}}`

- 포트에서 VLAN 제거:

`sudo bridge {{[v|vlan]}} {{[d|delete]}} dev {{lanX}} vid {{vlan_id}}`

- 브릿지 인터페이스 변경 사항 모니터링:

`bridge {{[mo|monitor]}}`

- 도움말 표시:

`bridge {{[h|help]}}`

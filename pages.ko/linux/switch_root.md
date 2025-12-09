# switch_root

> 다른 파일 시스템을 마운트 트리의 루트로 사용.
> 참고: 새 루트가 마운트의 루트가 아닌 경우, switch_root는 작동하지 않습니다. 바인드 마운트를 사용하여 이를 해결할 수 있습니다.
> 같이 보기: `chroot`, `mount`.
> 더 많은 정보: <https://manned.org/switch_root.8>.

- `/proc`, `/dev`, `/sys` 및 `/run`을 지정한 파일 시스템으로 이동하고, 해당 파일 시스템을 새로운 루트로 사용하여 지정한 초기화 프로세스를 시작:

`switch_root {{새_루트}} {{/sbin/init}}`

- 도움말 표시:

`switch_root -h`

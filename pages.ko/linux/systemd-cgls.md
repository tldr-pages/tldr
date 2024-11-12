# systemd-cgls

> 선택된 Linux 제어 그룹 계층의 내용을 트리 형태로 보여줍니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>.

- 시스템의 전체 제어 그룹 계층 표시:

`systemd-cgls`

- 특정 리소스 컨트롤러의 제어 그룹 트리 표시:

`systemd-cgls {{cpu|memory|io}}`

- 하나 이상의 systemd 유닛의 제어 그룹 계층 표시:

`systemd-cgls --unit {{unit1 unit2 ...}}`

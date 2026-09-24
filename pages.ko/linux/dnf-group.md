# dnf group

> Fedora 계열 시스템에서 가상 패키지 그룹 관리.
> 더 많은 정보: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- 설치 여부 상태와 함께 DNF 그룹 목록을 테이블 형태로 표시:

`dnf {{[grp|group]}} list`

- 저장소 정보 및 선택 패키지를 포함한 DNF 그룹 정보 표시:

`dnf {{[grp|group]}} info {{그룹_이름}}`

- DNF 그룹 설치:

`dnf {{[grp|group]}} install {{그룹_이름}}`

- DNF 그룹 제거:

`dnf {{[grp|group]}} remove {{그룹_이름}}`

- DNF 그룹 업그레이드:

`dnf {{[grp|group]}} upgrade {{그룹_이름}}`

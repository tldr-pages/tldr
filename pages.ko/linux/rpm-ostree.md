# rpm-ostree

> 하이브리드 이미지/패키지 시스템.
> ostree 배포, 패키지 레이어, 파일시스템 오버레이 및 부트 구성을 관리합니다.
> 더 많은 정보: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- 부트로더에 나타날 순서대로 rpm-ostree 배포 표시:

`rpm-ostree status`

- 업데이트할 수 있는 오래된 패키지 표시:

`rpm-ostree upgrade --preview`

- 패키지를 업그레이드하고 새로운 ostree 배포 준비 후 재부팅:

`rpm-ostree upgrade --reboot`

- 이전 ostree 배포로 재부팅:

`rpm-ostree rollback --reboot`

- 새 ostree 배포에 패키지를 설치하고 그곳으로 재부팅:

`rpm-ostree install {{패키지}} --reboot`

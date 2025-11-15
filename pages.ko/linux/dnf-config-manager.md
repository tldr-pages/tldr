# dnf config-manager

> Fedora 기반 시스템에서 DNF 구성 옵션과 저장소를 관리합니다.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- URL에서 저장소 추가(그리고 활성화):

`dnf config-manager --add-repo={{저장소_URL}}`

- 현재 구성 값 출력:

`dnf config-manager --dump`

- 특정 저장소 활성화:

`dnf config-manager --set-enabled {{저장소_ID}}`

- 지정된 저장소 비활성화:

`dnf config-manager --set-disabled {{저장소_ID1 저장소_ID2 ...}}`

- 저장소에 대한 구성 옵션 설정:

`dnf config-manager --setopt={{옵션}}={{값}}`

- 도움말 표시:

`dnf config-manager --help-cmd`

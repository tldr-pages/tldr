# quickget

> Quickemu 가상 머신 빌드를 위한 자료를 다운로드하고 준비합니다.
> 참고: "edition" 매개변수는 항상 선택 사항입니다.
> 같이 보기: `quickemu`.
> 더 많은 정보: <https://github.com/quickemu-project/quickemu>.

- 지원되는 모든 게스트 운영 체제, 버전 및 변형 목록 표시:

`quickget list`

- 운영 체제에 대한 Quickemu 가상 머신을 빌드하기 위한 가상 머신 설정 다운로드 및 생성:

`quickget {{os}} {{release}} {{edition}}`

- VirtIO 드라이버가 포함된 Windows 11 VM 설정 다운로드:

`quickget windows 11`

- macOS 복구 이미지를 다운로드하고 가상 머신 설정 생성:

`quickget macos {{mojave|catalina|big-sur|monterey|ventura|sonoma}}`

- 운영 체제의 ISO URL 표시:

`quickget --url fedora {{release}} {{edition}}`

- 운영 체제에 대한 ISO 파일이 있는지 테스트:

`quickget --check nixos {{release}} {{edition}}`

- VM 설정을 빌드하지 않고 이미지 다운로드:

`quickget --download {{os}} {{release}} {{edition}}`

- 운영 체제 이미지에 대한 VM 설정 생성:

`quickget --create-config {{os}} {{경로/대상/iso}}`

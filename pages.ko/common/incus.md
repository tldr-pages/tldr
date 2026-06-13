# incus

> 현대적이고, 보안성이 뛰어나며 강력한 시스템 컨테이너 및 가상 머신 관리자.
> 더 많은 정보: <https://linuxcontainers.org/incus/docs/main/>.

- 모든 컨테이너 및 가상 머신 목록 출력 (실행 중 및 중지 상태 모두 포함):

`incus list`

- 이미지로부터 컨테이너 생성 (사용자 지정 이름):

`incus create {{image}} {{컨테이너_이름}}`

- 기존 컨테이너 시작 또는 중지:

`incus {{start|stop}} {{컨테이너_이름}}`

- 실행 중인 컨테이너 내부에서 쉘 실행:

`incus shell {{컨테이너_이름}}`

- 중지된 컨테이너 삭제:

`incus delete {{컨테이너_이름}}`

- 원격 (remote) 이미지 저장소에서 로컬로 이미지 가져오기:

`incus copy {{remote}}:{{이미지}} local:{{커스텀_이미지_이름}}`

- 공식 `images:` 원격 저장소에서 사용 가능한 이미지 출력:

`incus image list images:`

- `local:`에 이미 다운로드된 이미지 목록 출력:

`incus image list local:`

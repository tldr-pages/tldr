# sgdisk

> GUID Partition Tables (GPT)을 관리.
> GPT fdisk 도구 모음의 일부, 스크립팅 및 자동화에 적합하도록 설계됨.
> 더 많은 정보: <https://manned.org/sgdisk>.

- 장치의 기본 GPT 파티션 요약 정보 표시:

`sudo sgdisk {{[-p|--print]}} {{/dev/sdX}}`

- 장치에서 GPT와 MBR 데이터 구조를 모두 삭제 (모든 파티션 정보 삭제):

`sudo sgdisk {{[-Z|--zap-all]}} {{/dev/sdX}}`

- 최대 4개의 파티션을 사용하여 GPT 디스크를 MBR 형식으로 변환:

`sudo sgdisk {{[-m|--gpttombr]}} {{1:2:3:4}} {{/dev/sdX}}`

- 번호를 지정하여 파티션 항목 삭제 (섹터의 데이터는 그대로 유지):

`sudo sgdisk {{[-d|--delete]}} {{1}} {{/dev/sdX}}`

- 현재 메모리에 있는 GPT 데이터를 (보호 MBR, 헤더 및 테이블) 바이너리 백업 파일로 저장:

`sudo sgdisk {{[-b|--backup]}} {{/경로/대상/백업파일.gpt}} {{/dev/sdX}}`

- 백업 파일에서 GPT 데이터 불러오기 (원본이 아닌 디스크에 복원하는 것은 권장되지 않음):

`sudo sgdisk {{[-l|--load-backup]}} {{/경로/대상/백업파일.gpt}} {{/dev/sdX}}`

- GPT 구조의 CRC 오류, 불일치 또는 비정상 상태 검사:

`sudo sgdisk {{[-v|--verify]}} {{/dev/sdX}}`

- 사용 가능한 파티션 유형 코드 요약 표시 (장치 지정 불필요):

`sgdisk {{[-L|--list-types]}}`

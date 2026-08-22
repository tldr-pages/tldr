# sg_raw

> 연결된 장치에 임의의 SCSI 명령을 전송.
> 더 많은 정보: <https://manned.org/sg_raw>.

- `sr0`에 할당된 광학 SCSI 장치에 명령을 전송하여 트레이의 미디어 로드:

`sg_raw /dev/sr0 EA 00 00 00 00 01`

- `stdin` 대신 `IFILE`에서 입력 데이터 읽기:

`sg_raw {{[-i|--infile]}} {{경로/대상/IFILE}} {{/dev/sgX}} {{scsi_명령어}}`

- 입력 데이터의 처음 `LEN` 바이트 건너뛰기:

`sg_raw {{[-k|--skip]}} {{LEN}} {{/dev/sgX}} {{scsi_명령어}}`

- `SLEN` 바이트의 데이터를 읽어 장치로 전송:

`sg_raw {{[-s|--send]}} {{SLEN}} {{/dev/sgX}} {{scsi_명령어}}`

- `sg_raw` 처리가 완료될 때까지 최대 `SEC`초 대기:

`sg_raw {{[-t|--timeout]}} {{SEC}} {{/dev/sgX}} {{scsi_명령어}}`

- 상세 출력 수준을 1 증가:

`sg_raw {{[-v|--verbose]}} {{/dev/sgX}} {{scsi_명령어}}`

- 반환된 데이터를 바이너리 형식으로 출력:

`sg_raw {{[-b|--binary]}} {{/dev/sgX}} {{scsi_명령어}}`

- 지정한 장치에서 수신한 데이터를 `OFILE`에 저장:

`sg_raw {{[-o|--outfile]}} {{경로/대상/OFILE}} {{/dev/sgX}} {{scsi_명령어}}`

# synoupgrade

> Synology DiskStation Manager (DSM) - Synology NAS 운영 체제 업그레이드.
> 더 많은 정보: <https://www.synology.com/dsm>.

- 업그레이드 가능 여부 확인:

`sudo synoupgrade --check`

- DSM 버전을 업그레이드하지 않고 패치 확인:

`sudo synoupgrade --check-smallupdate`

- 사용 가능한 최신 업그레이드 다운로드 (`--download-smallupdate`로 패치 다운로드 가능):

`sudo synoupgrade --download`

- 업그레이드 프로세스 시작:

`sudo synoupgrade --start`

- 최신 버전으로 자동 업그레이드:

`sudo synoupgrade --auto`

- DSM 버전을 업그레이드하지 않고 자동으로 패치 적용:

`sudo synoupgrade --auto-smallupdate`

- 패치 파일을 사용하여 DSM 업그레이드 (절대 경로여야 함):

`sudo synoupgrade --patch {{/경로/대상/파일.pat}}`

- 도움말 표시:

`synoupgrade`

# autopsy

> 디스크 이미지 분석과 파일 시스템 조사를 위한 디지털 포렌식 플랫폼.
> 더 많은 정보: <https://sleuthkit.org/autopsy/docs/user-docs/4.14.0/command_line_ingest_page.html>.

- Autopsy 그래픽 인터페이스 실행:

`autopsy64.exe`

- 새로운 사건을 생성하고 사건 파일을 저장할 기본 디렉터리 지정:

`autopsy64.exe --createCase --caseName {{case_이름}} --caseBaseDir {{경로\대상\base_디렉터리}}`

- 기존 사건에 데이터 소스 추가:

`autopsy64.exe --caseDir {{경로\대상\case_디렉터리}} --addDataSource --dataSourcePath {{경로\대상\소스파일}}`

- 기존 사건의 보고서 생성:

`autopsy64.exe --caseDir {{경로\대상\case_디렉터리}} --generateReports`

- 기존 사건의 모든 데이터 소스 목록 표시:

`autopsy64.exe --caseDir {{경로\대상\case_디렉터리}} --listAllDataSources`

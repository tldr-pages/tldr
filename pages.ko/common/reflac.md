# reflac

> FLAC 파일을 메타데이터를 유지하며 제자리에서 재압축.
> 더 많은 정보: <https://github.com/chungy/reflac>.

- FLAC 파일이 있는 디렉토리 재압축:

`reflac {{경로/대상/폴더}}`

- 최대 압축 사용 (매우 느림):

`reflac --best {{경로/대상/폴더}}`

- 처리 중인 파일 이름 표시:

`reflac --verbose {{경로/대상/폴더}}`

- 하위 디렉토리까지 재귀적으로 처리:

`reflac --recursive {{경로/대상/폴더}}`

- 파일 수정 시간 보존:

`reflac --preserve {{경로/대상/폴더}}`

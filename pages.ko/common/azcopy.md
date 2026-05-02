# azcopy

> Azure Storage로 데이터를 복사하거나 Azure Storage에서 데이터를 복사.
> 관련 항목: `az storage`.
> 더 많은 정보: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10#list-of-commands>.

- Azure Tenant에 로그인:

`azcopy login`

- 로컬 파일을 업로드:

`azcopy {{[c|copy]}} '{{경로/대상/소스_파일}}' 'https://{{저장소_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}/{{blob_이름}}'`

- `.txt` 및 `.jpg` 확장자를 가진 파일을 업로드:

`azcopy {{[c|copy]}} '{{경로/대상/소스_디렉토리}}' 'https://{{저장소_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' --include-pattern '*.txt;*.jpg'`

- 두 Azure storage 계정 간에 컨테이너를 직접 복사:

`azcopy {{[c|copy]}} 'https://{{소스_저장소_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' 'https://{{목표_저장소_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}'`

- 로컬 디렉터리를 동기화하고, 원본에 더 이상 존재하지 않는 파일은 대상에서 삭제:

`azcopy {{[s|sync]}} '{{path/to/source_directory}}' 'https://{{저장소_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' --delete-destination true`

- 도움말 표시:

`azcopy {{[-h|--help]}}`

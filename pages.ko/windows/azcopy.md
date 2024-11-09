# azcopy

> Azure 클라우드 스토리지 계정에 업로드하기 위한 파일 전송 도구.
> 더 많은 정보: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Azure 테넌트에 로그인:

`azopy login`

- 로컬 파일 업로드:

`azcopy copy '{{경로\대상\소스_파일}}' 'https://{{스토리지_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}/{{블롭_이름}}'`

- `.txt` 및 `.jpg` 확장자를 가진 파일 업로드:

`azcopy copy '{{경로\대상\소스_폴더}}' 'https://{{스토리지_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' --include-pattern '{{*.txt;*.jpg}}'`

- 두 Azure 스토리지 계정 간에 컨테이너 직접 복사:

`azcopy copy 'https://{{소스_스토리지_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' 'https://{{목적지_스토리지_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}'`

- 로컬 디렉터리와 동기화하고 소스에 더 이상 존재하지 않는 파일을 대상에서 삭제:

`azcopy sync '{{경로\대상\소스_폴더}}' 'https://{{스토리지_계정_이름}}.blob.core.windows.net/{{컨테이너_이름}}' --recursive --delete-destination=true`

- 도움말 표시:

`azcopy --help`

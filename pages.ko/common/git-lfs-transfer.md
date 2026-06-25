# git-lfs-transfer

> Git LFS 순수 SSH 전송 프로토콜의 서버 측 구현.
> Git LFS가 HTTPS 대신 SSH를 통해 대용량 파일을 업로드 및 다운로드할 수 있도록 지원.
> 더 많은 정보: <https://github.com/charmbracelet/git-lfs-transfer#usage>.

- Git LFS로 추적되는 대용량 파일을 저장소에 업로드:

`git-lfs-transfer {{경로/대상/저장소.git}} upload`

- Git LFS로 추적되는 대용량 파일을 저장소에서 다운로드:

`git-lfs-transfer {{경로/대상/저장소.git}} download`

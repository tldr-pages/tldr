# bfg

> git-filter-branch와 같은 Git 기록에서 대용량 파일이나, 비밀번호를 제거.
> 참고: 저장소가 원격 장치에 연결되어 있으면, 강제로 푸시해야 함.
> 더 많은 정보: <https://rtyley.github.io/bfg-repo-cleaner/>.

- 민감한 데이터가 포함된 파일을 제거하되 최신 커밋은 그대로 유지:

`bfg --delete-files {{민감한_데이터가_포함된_파일}}`

- 저장소 기록에서 찾을 수 있는 특정 파일에 언급된 모든 텍스트를 제거:

`bfg --replace-text {{경로/대상/파일.txt}}`

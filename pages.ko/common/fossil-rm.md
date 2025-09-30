# fossil rm

> Fossil 버전 관리에서 파일이나 디렉터리를 제거.
> 참고: `fossil forget`.
> 더 많은 정보: <https://fossil-scm.org/home/help/rm>.

- Fossil 버전 관리에서 파일이나 디렉터리를 제거:

`fossil rm {{경로/대상/파일_또는_디렉토리}}`

- Fossil 버전 관리에서 파일이나 디렉터리를 제거하고, 디스크에서도 삭제:

`fossil rm --hard {{경로/대상/파일_또는_디렉토리}}`

- 이전에 제거하고 커밋하지 않은 모든 파일을 Fossil 버전 관리에 다시 추가:

`fossil rm --reset`

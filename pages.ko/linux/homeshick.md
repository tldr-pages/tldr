# homeshick

> Git dotfiles를 동기화합니다.
> 같이 보기: `chezmoi`, `stow`, `tuckr`, `vcsh`.
> 더 많은 정보: <https://github.com/andsens/homeshick/wiki>.

- 새로운 성(castle) 생성:

`homeshick generate {{성_이름}}`

- 성에 파일 추가:

`homeshick track {{성_이름}} {{경로/대상/파일}}`

- 성으로 이동:

`homeshick cd {{성_이름}}`

- 성 복제:

`homeshick clone {{GitHub_사용자명}}/{{저장소_이름}}`

- 성의 모든 파일을 심볼릭 링크로 연결:

`homeshick link {{성_이름}}`

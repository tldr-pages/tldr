# scrontab

> Slurm 크론탭 파일을 관리합니다.
> 더 많은 정보: <https://slurm.schedmd.com/scrontab.html>.

- 지정된 파일에서 새 크론탭 설치:

`scrontab {{경로/대상/파일}}`

- 현재 사용자의 크론탭 [e]편집:

`scrontab -e`

- 지정된 사용자의 크론탭 [e]편집:

`scrontab --user={{사용자_ID}} -e`

- 현재 크론탭 [r]제거:

`scrontab -r`

- 현재 사용자의 크론탭을 `stdout`에 출력:

`scrontab -l`

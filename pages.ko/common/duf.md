# duf

> 디스크 사용량/무료 유틸리티.
> 더 많은 정보: <https://github.com/muesli/duf>.

- 접근 가능한 장치 목록:

`duf`

- 모든 항목을 나열 (예: 의사, 중복 또는 액세스할 수 없는 파일 시스템):

`duf --all`

- 지정된 장치 또는 마운트 지점만 표시:

`duf {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`

- 지정된 기준에 따라 출력 결과를 정렬:

`duf --sort {{size|used|avail|usage}}`

- 특정 파일 시스템을 표시하거나 숨김:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- 키별로 출력을 정렬:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- 테마를 변경 (`duf`가 올바른 테마를 사용하지 못하는 경우):

`duf --theme {{dark|light}}`

# parted

> 파티션 조작 프로그램.
> 같이 보기: `partprobe`.
> 더 많은 정보: <https://www.gnu.org/software/parted/manual/parted.html#Invoking-Parted>.

- 모든 블록 디바이스의 파티션 나열:

`sudo parted --list`

- 지정된 디스크를 선택하여 대화형 모드 시작:

`sudo parted {{/dev/sdX}}`

- 지정된 레이블 유형의 새 파티션 테이블 생성:

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- 대화형 모드에서 파티션 정보 표시:

`print`

- 대화형 모드에서 디스크 선택:

`select {{/dev/sdX}}`

- 대화형 모드에서 지정된 파일 시스템으로 16GB 파티션 생성:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- 대화형 모드에서 파티션 크기 조정:

`resizepart {{/dev/sdXN}} {{파티션_끝_위치}}`

- 대화형 모드에서 파티션 제거:

`rm {{/dev/sdXN}}`

# diffoscope

> 파일, 아카이브 및 디렉터리를 비교.
> 더 많은 정보: <https://diffoscope.org>.

- 2개 파일 비교:

`diffoscope {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 진행 표시줄을 보여주지 않고 두 파일을 비교:

`diffoscope --no-progress {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 두 파일을 비교하고 HTML 보고서를 파일에 작성 (`stdout`에는 `-` 사용):

`diffoscope --html {{경로/대상/출력파일|-}} {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 지정된 패턴과 일치하는 이름을 가진 파일을 제외한 두 디렉터리를 비교:

`diffoscope --exclude {{패턴}} {{경로/대상/디렉터리1}} {{경로/대상/디렉터리2}}`

- 두 디렉터리를 비교하고 디렉터리 메타데이터가 고려되는지 여부를 제어:

`diffoscope --exclude-directory-metadata {{auto|yes|no|recursive}} {{경로/대상/디렉터리1}} {{경로/대상/디렉터리2}}`

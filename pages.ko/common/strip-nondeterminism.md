# strip-nondeterminism

> 파일에서 비결정적인 정보(예: 타임스탬프)를 제거.
> 더 많은 정보: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>.

- 파일에서 비결정적인 정보 제거:

`strip-nondeterminism {{경로/대상/파일}}`

- 파일 유형을 수동으로 지정하여 파일에서 비결정적인 정보 제거:

`strip-nondeterminism --type {{파일유형}} {{경로/대상/파일}}`

- 파일에서 비결정적인 정보를 제거하되, 타임스탬프를 제거하는 대신 지정한 UNIX 타임스탬프로 설정:

`strip-nondeterminism --timestamp {{유닉스_타임스탬프}} {{경로/대상/파일}}`

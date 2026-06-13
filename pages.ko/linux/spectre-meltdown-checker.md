# spectre-meltdown-checker

> Spectre와 Meltdown 완화 감지 도구.
> 더 많은 정보: <https://manned.org/spectre-meltdown-checker>.

- 현재 실행 중인 커널을 Spectre 또는 Meltdown에 대해 검사:

`sudo spectre-meltdown-checker`

- 현재 실행 중인 커널을 검사하고 취약성을 완화하기 위한 조치 설명 표시:

`sudo spectre-meltdown-checker --explain`

- 특정 변종 검사 (기본적으로 모두 검사):

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- 특정 출력 형식을 사용하여 출력 표시:

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- `/sys` 인터페이스가 존재해도 사용하지 않음:

`sudo spectre-meltdown-checker --no-sysfs`

- 실행 중이지 않은 커널 검사:

`sudo spectre-meltdown-checker --kernel {{경로/대상/커널_파일}}`

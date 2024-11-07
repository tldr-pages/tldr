# mh_metric

> MATLAB 또는 Octave 코드의 코드 메트릭을 계산하고 적용.
> 더 많은 정보: <https://misshit.org>.

- 지정된 파일의 코드 메트릭 출력:

`mh_metric {{경로/대상/파일1.m 경로/대상/파일2.m ...}}`

- 지정된 Octave 파일의 코드 메트릭 출력:

`mh_metric --octave {{경로/대상/파일1.m 경로/대상/파일2.m ...}}`

- 지정된 디렉터리의 코드 메트릭을 재귀적으로 출력:

`mh_metric {{경로/대상/폴더}}`

- 현재 디렉터리의 코드 메트릭 출력:

`mh_metric`

- 코드 메트릭 보고서를 HTML 또는 JSON 형식으로 출력:

`mh_metric --{{html|json}} {{경로/대상/출력_파일}}`

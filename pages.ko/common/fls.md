# fls

> 이미지 파일이나 장치의 파일과 디렉터리를 나열.
> 더 많은 정보: <https://wiki.sleuthkit.org/index.php?title=Fls>.

- 장치에 대한 재귀 fls 목록을 작성하면, 출력 경로가 C로 시작:

`fls -r -m {{C:}} {{/dev/loop1p1}}`

- 단일 파티션을 분석하여 이미지에서 파일 시스템이 시작되는 섹터 오프셋을 제공:

`fls -r -m {{C:}} -o {{sector}} {{경로/대상/이미지_파일}}`

- 단일 파티션을 분석하여, 원래 시스템의 시간대를 제공:

`fls -r -m {{C:}} -z {{timezone}} {{/dev/loop1p1}}`

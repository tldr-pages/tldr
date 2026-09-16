# pocount

> 다양한 형식을 지원하는 번역 파일의 번역 진행 상황을 확인하는 Toolkit 유틸리티.
> 더 많은 정보: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- 파일의 번역 진행 상황을 컬러 테이블로 표시:

`pocount {{경로/대상/파일.po}}`

- 여러 파일의 번역 진행 상황을 파일 당 한 줄씩 표시:

`pocount --short {{translation_*.ts}}`

- 여러 파일의 번역 진행 상황을 CSV 파일로 생성:

`pocount --csv {{translation_*.ts}} > {{경로/대상/번역_진행상황.csv}}`

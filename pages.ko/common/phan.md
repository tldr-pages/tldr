# phan

> PHP용 정적 분석 도구.
> 더 많은 정보: <https://github.com/phan/phan>.

- 현재 디렉터리에 `.phan/config.php` 생성:

`phan --init`

- 특정 레벨을 사용하여 Phan 구성 파일 생성 (1이 가장 엄격하고 5가 가장 덜 엄격함):

`phan --init --init-level {{레벨}}`

- 현재 디렉터리 분석:

`phan`

- 하나 이상의 디렉터리 분석:

`phan --directory {{경로/대상/폴더}} --directory {{경로/대상/다른_폴더}}`

- 구성 파일 지정 (기본값은 `.phan/config.php`):

`phan --config-file {{경로/대상/config.php}}`

- 출력 모드 지정:

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- 병렬 프로세스 수 지정:

`phan --processes {{프로세스_수}}`

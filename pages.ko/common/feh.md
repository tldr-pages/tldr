# feh

> 경량 이미지 보기 유틸리티.
> 더 많은 정보: <https://man.finalrewind.org/1/feh/>.

- 로컬에서 또는 URL을 사용하여 이미지 보기:

`feh {{경로/대상/이미지}}`

- 재귀적으로 이미지 보기:

`feh --recursive {{경로/대상/이미지}}`

- 창 테두리 없이 이미지 보기:

`feh --borderless {{경로/대상/이미지}}`

- 마지막 이미지 이후 종료:

`feh --cycle-once {{경로/대상/이미지}}`

- 특정 슬라이드쇼 주기 지연을 사용:

`feh --slideshow-delay {{초}} {{경로/대상/이미지}}`

- 특정 배경화면 모드 사용 (중앙 맞춤, 채우기, 최대화, 크기 조정 또는 타일링):

`feh --bg-{{center|fill|max|scale|tile}} {{경로/대상/이미지}}`

- 디렉터리 내 모든 이미지의 몽타주를 생성하여 새 이미지로 출력:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{경로/대상/몽타주_이미지}}`

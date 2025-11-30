# rspec

> Ruby 코드를 테스트하기 위한 Ruby로 작성된 행동 주도 개발 테스트 프레임워크.
> 더 많은 정보: <https://rspec.info/features/3-13/rspec-core/command-line/>.

- .rspec 구성 파일과 spec 헬퍼 파일 초기화:

`rspec --init`

- 모든 테스트 실행:

`rspec`

- 특정 디렉터리의 테스트 실행:

`rspec {{경로/대상/폴더}}`

- 하나 이상의 테스트 파일 실행:

`rspec {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 파일 내 특정 테스트 실행 (예: 테스트가 83번째 줄에서 시작하는 경우):

`rspec {{경로/대상/파일}}:{{83}}`

- 특정 시드로 스펙 실행:

`rspec --seed {{시드_번호}}`

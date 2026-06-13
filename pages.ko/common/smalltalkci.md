# smalltalkci

> GitHub Actions, Travis CI, AppVeyor, GitLab CI 등과 함께 Smalltalk 프로젝트를 테스트하기 위한 프레임워크.
> 더 많은 정보: <https://github.com/hpi-swa/smalltalkCI>.

- 구성 파일에 대한 테스트 실행:

`smalltalkci {{경로/대상/.smalltalk.ston}}`

- 현재 디렉토리의 `.smalltalk.ston` 구성에 대한 테스트 실행:

`smalltalkci`

- GUI 모드에서 테스트 디버그 (VM 창 표시):

`smalltalkci --headful`

- 테스트를 위한 잘 알려진 Smalltalk 이미지 다운로드 및 준비:

`smalltalkci --smalltalk {{Squeak64-Trunk}}`

- 사용자 지정 Smalltalk 이미지 및 VM 지정:

`smalltalkci --image {{경로/대상/Smalltalk.image}} --vm {{경로/대상/vm}}`

- 캐시 정리 및 빌드 삭제:

`smalltalkci --clean`

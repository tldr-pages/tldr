# b4 am

> public-inbox 아카이브에서 패치를 가져와 `git am`으로 적용할 수 있도록 준비.
> 더 많은 정보: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- 스레드에서 패치를 가져와 `git am`용으로 준비:

`b4 am {{메시지_아이디}}`

- 모든 커밋에 자신의 `Signed-off-by`와 `Link:` 트레일러를 추가하여 패치 준비:

`b4 am {{[-sl|--add-my-sob --add-link]}} {{메시지_아이디}}`

- 충돌 해결을 위한 3-way 병합 지원과 함께 패치 준비:

`b4 am {{[-3|--prep-3way]}} {{메시지_아이디}}`

- 패치 시리즈에서 지정한 패치만 Cherry-pick하여 준비 (예: 패치 1-3, 5번 적용):

`b4 am {{[-P|--cherry-pick]}} {{1-3,5}} {{메시지_아이디}}`

- 패치를 가져오고 각 패치에 대해 로컬 검사 수행:

`b4 am --check {{메시지_아이디}}`

- 출력된 메일박스를 지정한 디렉터리에 저장:

`b4 am {{[-o|--outdir]}} {{경로/대상/디렉터리}} {{메시지_아이디}}`

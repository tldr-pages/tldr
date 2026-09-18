# b4 shazam

> public-inbox 아카이브에서 패치를 가져와 현재 Git 작업 트리에 직접 적용.
> 더 많은 정보: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- 스레드에서 패치를 가져와 현재 브랜치에 적용:

`b4 shazam {{메시지_아이디}}`

- 패치를 가져와 병합할 수 있도록 `FETCH_HEAD` 생성 (pull request 방식):

`b4 shazam {{[-H|--make-fetch-head]}} {{메시지_아이디}}`

- 패치를 가져오고 커버 레터(cover letter)를 병합 커밋 메시지로 사용하여 자동 병합:

`b4 shazam {{[-M|--merge]}} {{메시지_아이디}}`

- 패치를 가져오고, 자신의 `Signed-off-by`와 `Link:` 트레일러를 추가하고 병합:

`b4 shazam {{[-slM|--add-my-sob --add-link --merge]}} {{메시지_아이디}}`

- 패치를 가져오고 필요한 경우 대화형으로 conflict 해결 시작:

`b4 shazam {{[-H|--make-fetch-head]}} --resolve {{메시지_아이디}}`

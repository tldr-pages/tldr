# gum

> 매력적인 쉘 스크립트 만들기.
> 더 많은 정보: <https://github.com/charmbracelet/gum#tutorial>.

- `stdout`으로 출력할 특정 옵션을 대화형으로 선택:

`gum choose "{{옵션_1}}" "{{옵션_2}}" "{{옵션_3}}"`

- 사용자가 특정 자리 표시자와 함께 문자열을 입력할 수 있는 대화형 프롬프트를 열기:

`gum input --placeholder "{{값}}"`

- 대화형 확인 프롬프트를 열고 `<0>` 또는 `<1>`로 종료:

`gum confirm "{{Continue?}}" --default=false --affirmative "{{Yes}}" --negative "{{No}}" {{&& echo "Yes selected" || echo "No selected"}}`

- 명령이 실행되는 동안 텍스트와 함께 스피너를 표시:

`gum spin --spinner {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{loading...}}" -- {{명령어}}`

- 이모티콘을 포함하도록 텍스트 형식을 지정:

`gum format -t {{emoji}} "{{:smile: :heart: hello}}"`

- 여러 줄의 텍스트를 대화식으로 프롬프트하고 (저장하려면 `<Ctrl d>`) `data.txt`에 작성:

`gum write > {{data.txt}}`

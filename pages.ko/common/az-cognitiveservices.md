# az cognitiveservices

> Azure Cognitive Services 계정을 관리하는 명령어.
> `azure-cli`의 일부 (`az`).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/cognitiveservices>.

- 특정 지역에 확인 없이 API Cognitive Services 계정 생성:

`az cognitiveservices account create {{[-n|--name]}} {{계정_이름}} {{[-g|--resource-group]}} {{리소스_그룹}} --kind {{api_이름}} {{[-l|--location]}} {{location}} --sku {{sku_이름}} --yes`

- Azure Cognitive Services 계정 사용량 조회:

`az cognitiveservices account list-usage {{[-n|--name]}} {{계정_이름}} {{[-g|--resource-group]}} {{리소스_그룹}}`

- Azure Cognitive Services 계정에 배포 생성:

`az cognitiveservices account deployment create {{[-n|--name]}} {{계정_이름}} {{[-g|--resource-group]}} {{리소스_그룹}} --deployment-name {{배포_이름}} --model-name {{모델_이름}} --model-version "{{모델_버전}}" --model-format {{포맷_이름}}`

- Azure Cognitive Services 계정에 커밋 플랜 생성:

`az cognitiveservices account commitment-plan create {{[-n|--name]}} {{계정_이름}} {{[-g|--resource-group]}} {{리소스_그룹}} --commitment-plan-name "{{plan_name}}" --hosting-model "{{호스팅_모델}}" --plan-type "{{플랜_타입}}" --auto-renew {{false|true}}`

- Azure Cognitive Services 계정에서 커밋 플랜 삭제:

`az cognitiveservices account commitment-plan delete {{[-g|--resource-group]}} {{리소스_그룹}} {{[-n|--name]}} {{계정_이름}} --commitment-plan-name "{{플랜_이름}}"`

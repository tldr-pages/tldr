# aws quicksight

> AWS QuickSight 엔터티를 생성, 삭제, 나열, 검색 및 업데이트.
> 더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- 데이터셋 나열:

`aws quicksight list-data-sets --aws-account-id {{aws_계정_아이디}}`

- 사용자 나열:

`aws quicksight list-users --aws-account-id {{aws_계정_아이디}} --namespace default`

- 그룹 나열:

`aws quicksight list-groups --aws-account-id {{aws_계정_아이디}} --namespace default`

- 대시보드 나열:

`aws quicksight list-dashboards --aws-account-id {{aws_계정_아이디}}`

- 데이터 세트에 대한 자세한 정보 표시:

`aws quicksight describe-data-set --aws-account-id {{aws_계정_아이디}} --data-set-id {{데이터_셋_아이디}}`

- 데이터셋에 접근할 수 있는 사람과 해당 사용자가 데이터셋에서 수행할 수 있는 작업 종류를 표시:

`aws quicksight describe-data-set-permissions --aws-account-id {{aws_계정_아이디}} --data-set-id {{데이터_셋_아이디}}`

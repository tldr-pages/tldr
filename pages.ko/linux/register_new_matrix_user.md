# register_new_matrix_user

> 등록이 비활성화된 상태에서 홈 서버에 새 사용자 등록.
> 더 많은 정보: <https://manned.org/register_new_matrix_user>.

- 대화형으로 사용자 생성:

`register_new_matrix_user --config {{경로/대상/홈서버.yaml}}`

- 대화형으로 관리자 사용자 생성:

`register_new_matrix_user --config {{경로/대상/홈서버.yaml}} --admin`

- 비대화형으로 관리자 사용자 생성(권장하지 않음):

`register_new_matrix_user --config {{경로/대상/홈서버.yaml}} --user {{사용자명}} --password {{비밀번호}} --admin`

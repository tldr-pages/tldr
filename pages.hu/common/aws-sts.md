# aws sts

> A Security Token Service (STS) lehetővé teszi ideiglenes hitelesítő adatok kérését (IAM) felhasználók vagy szövetségi felhasználók számára. További információ: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Ideiglenes biztonsági hitelesítő adatok lekérése bizonyos AWS-erőforrásokhoz való hozzáféréshez:

`aws sts assume-role --role-arn {{aws_role_arn}}`

- Olyan IAM-felhasználó vagy szerepkör lekérése, amelynek hitelesítő adatai a művelet hívásához szükségesek:

`aws sts get-caller-identity`

#mockgen

> Mockgen is used to generate mock files for testing in go language
> It makes use of gomock, a framework for mocking in Go language


- From the filepath specified in source, generates a mock in the destination path along with package name

`mockgen -source={{{{source file path}} -destination={{destination file path}} -package={{packageName}}`

- Imports can also be added along with this to include any external repos

`mockgen -source={{{{source file path}} -destination={{destination file path}} -package={{packageName}} -imports={{imports to add}}`

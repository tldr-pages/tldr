> REST API Requests: <br>
> (N.B. the following examples work well with **Git Bash**: <br>
> Install Git from here: https://git-scm.com/downloads )

- Make a GET request:

`curl {https://example-api.com/endpoint}`

- Make a POST request:

'curl POST -d "userId=5&title={title_text_with_spaces_allowed}&body={body_text_with_spaces_allowed}" {https://example-api.com/endpoint}`

- Retrieve ('GET') the resource back:

`curl {https://example-api.com/endpoint/{parameter-eg-ID}}`

- Delete a resource:

`curl -X DELETE {https://example-api.com/endpoint/{parameter-eg-ID}}`

- Authorization:
  - Often provided with an OAuth token - request a token from the API provider
  - example usage: <br>
    `curl -H "Content-Type: application/json" -H "Authorization: "{token}"" -X POST -d "{"key1" : "value1", "key2" : "value2"}" {https://example.com/}`

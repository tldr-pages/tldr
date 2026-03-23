# supabase login

> Authenticate the Supabase CLI with a personal access token.
> More information: <https://supabase.com/docs/reference/cli/supabase-login>.

- Authenticate interactively (opens browser to generate a token):

`supabase login`

- Authenticate with a pre-generated access token:

`supabase login --token {{access_token}}`

- Authenticate without opening a browser:

`supabase login --no-browser`

- Store the token with a custom name:

`supabase login --name {{token_name}}`

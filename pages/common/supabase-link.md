# supabase link

> Link the local project to a remote Supabase project.
> Required before using remote database operations like `db push` or `db pull`.
> More information: <https://supabase.com/docs/reference/cli/supabase-link>.

- Link to a remote project by its reference ID:

`supabase link --project-ref {{project_ref}}`

- Link and provide the database password:

`supabase link --project-ref {{project_ref}} --password {{db_password}}`

- Link using a direct database connection instead of the connection pooler:

`supabase link --project-ref {{project_ref}} --skip-pooler`

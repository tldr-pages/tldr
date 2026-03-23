# supabase db pull

> Pull schema changes from a remote database and create a local migration file.
> Requires `supabase link` to be run first, or use `--db-url` for a custom database.
> More information: <https://supabase.com/docs/reference/cli/supabase-db-pull>.

- Pull schema from the linked remote project:

`supabase db pull`

- Pull schema from a custom database using a connection string:

`supabase db pull --db-url {{postgresql://user:password@host/database}}`

- Pull only specific schemas:

`supabase db pull --schema {{public,auth}}`

- Pull schema from the local development database:

`supabase db pull --local`

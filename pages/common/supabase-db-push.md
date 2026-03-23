# supabase db push

> Push local database migrations to a remote Supabase project.
> Requires `supabase link` to be run first, or use `--db-url` for a custom database.
> More information: <https://supabase.com/docs/reference/cli/supabase-db-push>.

- Push migrations to the linked remote project:

`supabase db push`

- Preview migrations without applying them:

`supabase db push --dry-run`

- Push to a custom database using a connection string:

`supabase db push --db-url {{postgresql://user:password@host/database}}`

- Push migrations including custom roles and seed data:

`supabase db push --include-roles --include-seed`

- Push to the local development database:

`supabase db push --local`

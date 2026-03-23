# supabase migration new

> Create a new timestamped migration file in `supabase/migrations`.
> More information: <https://supabase.com/docs/reference/cli/supabase-migration-new>.

- Create a new migration with a descriptive name:

`supabase migration new {{migration_name}}`

- Create a migration by piping the output of `supabase db diff`:

`supabase db diff | supabase migration new {{migration_name}}`

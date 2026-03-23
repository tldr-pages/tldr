# supabase gen types

> Generate type definitions from a Supabase database schema.
> Supports TypeScript, Go, Swift, and Python.
> More information: <https://supabase.com/docs/reference/cli/supabase-gen-types>.

- Generate TypeScript types from the local development database:

`supabase gen types --lang typescript --local`

- Generate TypeScript types from the linked remote project:

`supabase gen types --lang typescript --linked`

- Generate types and save to a file:

`supabase gen types --lang {{typescript|go|swift|python}} --local > {{path/to/output_file}}`

- Generate types for specific schemas only:

`supabase gen types --lang typescript --local --schema {{public,auth}}`

- Generate types from a specific project by ID:

`supabase gen types --lang typescript --project-id {{project_id}}`

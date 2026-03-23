# supabase stop

> Stop the local Supabase development stack.
> More information: <https://supabase.com/docs/reference/cli/supabase-stop>.

- Stop the local stack while preserving data in Docker volumes:

`supabase stop`

- Stop all local Supabase instances across all projects:

`supabase stop --all`

- Stop and permanently delete all local data:

`supabase stop --no-backup`

- Stop a specific project instance:

`supabase stop --project-id {{project_id}}`

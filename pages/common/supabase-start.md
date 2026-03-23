# supabase start

> Start the local Supabase development stack.
> Requires Docker to be running.
> More information: <https://supabase.com/docs/reference/cli/supabase-start>.

- Start all local Supabase services:

`supabase start`

- Start services while excluding specific ones:

`supabase start --exclude {{realtime,storage-api}}`

- Start services and ignore health check failures:

`supabase start --ignore-health-check`

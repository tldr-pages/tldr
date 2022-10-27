# Stormlock

> Centralized locking system.
> More information: <https://github.com/tmccombs/stormlock>.

- Acquire a lease for resource:

`stormlock acquire {{resource}}`

- Release the given lease for the given resource:

`stormlock release {{resource}} {{lease_id}}`

- Show information on the current lease for a resource, if any:

`stormlock current {{resource}}`

- Test if a lease for given resource is currently active:

`stormlock is-held {{resource}} {{lease_id}}`

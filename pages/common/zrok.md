# zrok

> Expose local services and files to the internet.
> Part of the OpenZiti project, offering secure, zero-trust sharing.
> More information: <https://docs.zrok.io>.

- Request an invitation to use the public zrok service (run this first):

`zrok invite`

- Enable the zrok environment with the token from an invitation email:

`zrok enable {{your_token}}`

- Create a publicly accessible URL for a local web server:

`zrok share public {{http://localhost:8080}}`

- Create a secure share accessible only with a unique token:

`zrok share private {{http://localhost:3000}}`

- Access a private share created by another user:

`zrok access private {{share_token}}`

- Serve the contents of a local directory as a simple website:

`zrok share public --backend-mode web {{path/to/directory}}`

- Display the status of the zrok environment and active shares:

`zrok status`

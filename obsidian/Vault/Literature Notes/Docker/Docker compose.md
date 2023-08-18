### command [link](https://docs.docker.com/compose/compose-file/05-services/#command)

`command` overrides the default command declared by the container image (i.e. by Dockerfile’s `CMD`).

```
command: bundle exec thin -p 3000
```

The value can also be a list, in a manner similar to [Dockerfile](https://docs.docker.com/engine/reference/builder/#cmd):

```
command: [ "bundle", "exec", "thin", "-p", "3000" ]
```

If the value is `null`, the default command from the image must be used.

If the value is `[]` (empty list) or `''` (empty string), the default command declared by the image must be ignored, i.e. overridden to be empty.


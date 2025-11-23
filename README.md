# Description
Kubernetes training Course deployed by [MkDocs](https://www.mkdocs.org/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) Docker Image

## Deploy

To deploy the course execute this command from the repository where the docs markdown resources folder exist:

```
$ docker run -d --name training-kubernetes -p 8001:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

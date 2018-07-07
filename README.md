# Install

## Ensure the `.env` file contains all necessary values as noted in the `.env.example` file.

## Ensure the `icecast.xml` file contains any additional hard-coded configuration options as needed.

** it's possible you'll need to modify the `templates/icecast.xml` file to suit your specific needs. The file as-is reflects the author's intended target and the `.env.example` contains example environment variables you may not (and probably will not) need/want.

## Run shell script
```
$ bash init.sh
```
(doesn't have to be bash of course)

This will install python dependencies and build the `icecast.xml` config file using the `template/icecast.xml` file, interpolating the values provided in the `.env` file.

## Build the Docker image
```
$ docker build -t your-image-name .
```

## The image is now ready to be deployed.

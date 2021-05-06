# capacity-hapi-fhir

## How to build the definition-importer docker image
First, download the 
[hapi-fhir cli](https://github.com/hapifhir/hapi-fhir/releases/download/v5.3.0/hapi-fhir-5.3.0-cli.tar.bz2) from 
github and place the archive in the subfolder `definition-importer`.

Then, you can build the image using docker-compose directly as follows:
```bash
docker-compose up -d --build
```

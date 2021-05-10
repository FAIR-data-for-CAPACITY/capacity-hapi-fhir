# capacity-hapi-fhir

## How to build the definition-importer docker image
First, download the 
[hapi-fhir cli](https://github.com/hapifhir/hapi-fhir/releases/download/v5.3.0/hapi-fhir-5.3.0-cli.tar.bz2) from 
github and place the archive in the subfolder `definition-importer`.

Then, you can build the image using docker-compose directly as follows:
```bash
docker-compose up -d --build
```
This will not only start the FHIR server, but also the `definition-importer` which will import standard codesystems listed in the FHIR spec into your FHIR server.
The fhir server will be running on `http://localhost:8080`.
When the `definition-importer` ends, you should be able to find a list of valuesets in the web browser. If the importer has failed, it will still be empty.

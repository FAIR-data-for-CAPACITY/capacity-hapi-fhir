# capacity-hapi-fhir

## Quickstart
1. Copy .env.example -> .env
2. Install the fhir client
    ```bash
   pip install -r requirements.txt
    ```
3. Run the hapi fhir server
    ```bash
   docker-compose up -d --build
    ```

## How to build and run.
Simply run the following command:
```bash
docker-compose up -d --build
```
This will not only start the FHIR server, but also the `definition-importer` which will import standard codesystems listed in the FHIR spec into your FHIR server.
The fhir server will be running on `http://localhost:8080`.
When the `definition-importer` ends, you should be able to find a list of valuesets in the web browser. If the importer has failed, it will still be empty.

## Aligning FHIR versions
There are several versions of the FHIR spec, and in various parts of this project this comes into play:
- HAPI FHIR server
- HAPI FHIR cli
- HAPI FHIR client

Because these are three different components, the FHIR version needs to be set in three different places. Currently, 
everything is set to STU3 by default but if you ever wish to change this to another version (e.g. R4) you will have 
to do the following:

1. The HAPI FHIR server and CLI version can be changed in one single step. Simply change the variable `FHIR_VERSION` 
   to the appropriate version in your `.env` file. Valid values are the values supported by the hapi fhir cli tool, 
   which are currently `dstu2`, `dstu3`, `r4`, `r5`.

   
2. The FHIR client needs to be set with ```pip install fhirclient==YOUR_FHIR_VERSION```. 
   Check the [FHIR client documentation](https://github.com/smart-on-fhir/client-py) how the fhir-client versions align
   with the official FHIR specs.
   
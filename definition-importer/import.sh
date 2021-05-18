#!/usr/bin/env bash

pip install fhirclient==$FHIRCLIENT_VERSION click tqdm

cd /mnt/definition-importer

python definition-importer.py --fhirversion $FHIR_VERSION --baseurl $BASE_URL
#!/usr/bin/env bash

FHIR_BASE=$1
FHIR_VERSION=$2

echo Filling server at $FHIR_BASE with definitions from FHIR version $FHIR_VERSION

./hapi-fhir-cli upload-definitions -t $FHIR_BASE -v $FHIR_VERSION

./hapi-fhir-cli upload-examples -t $FHIR_BASE -v $FHIR_VERSION
FROM continuumio/miniconda3

ENV BASE_URL=http://localhost:8080/fhir

# Available versions for FHIR_VERSION: dstu2, dstu3, r4, r5
ENV FHIR_VERSION=dstu3
ENV FHIRCLIENT_VERSION=3.0.0

RUN mkdir /app
RUN  pip install click tqdm

COPY definition-importer /app

WORKDIR /app

CMD pip install fhirclient==$FHIRCLIENT_VERSION && python definition-importer.py --fhirversion $FHIR_VERSION --baseurl $BASE_URL


FROM openjdk:17-buster

ENV FHIR_BASE=http://localhost:8080/fhir

# Available versions for FHIR_VERSION: dstu2, dstu3, r4, r5
ENV FHIR_VERSION=dstu3
ENV HAPI_CLI_URL=https://github.com/hapifhir/hapi-fhir/releases/download/v5.3.0/hapi-fhir-5.3.0-cli.tar.bz2

ARG TARGET_DIR=hapi-fhir-cli

RUN mkdir -p /app/$TARGET_DIR

WORKDIR /app/$TARGET_DIR
RUN curl -o archive.tar.bz2 -LJ $HAPI_CLI_URL && tar xjf archive.tar.bz2 && rm archive.tar.bz2

CMD ./hapi-fhir-cli upload-definitions -t $FHIR_BASE -v $FHIR_VERSION && ./hapi-fhir-cli upload-examples -t $FHIR_BASE -v $FHIR_VERSION
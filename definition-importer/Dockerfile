FROM openjdk:17-buster

ENV FHIR_BASE=http://localhost:8080/fhir
ENV FHIR_VERSION=dstu3
ARG TARGET_DIR=hapi-fhir-cli
ARG HAPI_FHIR_CLI_ARCHIVE=hapi-fhir-5.3.0-cli.tar.bz2

RUN mkdir /app /app/$TARGET_DIR
COPY $HAPI_FHIR_CLI_ARCHIVE /app/$HAPI_FHIR_CLI_ARCHIVE

WORKDIR /app
RUN tar xjf $HAPI_FHIR_CLI_ARCHIVE -C $TARGET_DIR

WORKDIR /app/$TARGET_DIR
CMD ./hapi-fhir-cli upload-definitions -t $FHIR_BASE -v $FHIR_VERSION
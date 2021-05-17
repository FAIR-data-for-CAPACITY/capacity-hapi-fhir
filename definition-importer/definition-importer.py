import json
from pathlib import Path
from urllib import request
from zipfile import ZipFile

import click
import requests
from tqdm import tqdm

SPEC_DOWNLOAD_TEMPLATE = 'http://hl7.org/fhir/{fhir_version}/definitions.json.zip'
EXAMPLE_DOWNLOAD_TEMPLATE = 'http://hl7.org/fhir/{fhir_version}/examples-json.zip'
STU3 = 'STU3'
DEFINITIONS_ARCHIVE = 'definitions.zip'
DEFINITIONS = 'definitions'
EXAMPLES = 'examples'
JSON_EXTENSION = '.json'
CACHE = 'cache'

OK_STATUS = {
    200,
    201,  # Resource has been created
    422  # Already exists
}


@click.command()
@click.option('--fhirversion', default=STU3, type=str)
@click.option('--baseurl', type=str)
def main(fhirversion, baseurl):
    process_definitions(baseurl, fhirversion)

    process_definitions(baseurl, fhirversion)


def process_definitions(baseurl, fhirversion):
    example_files = retrieve_definitions(EXAMPLE_DOWNLOAD_TEMPLATE.format(fhir_version=fhirversion))
    for file_path in tqdm(example_files):
        if file_path.name.endswith(JSON_EXTENSION):
            with file_path.open('r') as f:
                resource = json.load(f)

                resource_type = resource['resourceType']

                if resource_type == 'bundle':
                    upload_bundle(resource, baseurl)
                else:
                    upload_resource(baseurl, resource, resource_type)


def retrieve_definitions(definitions_url):
    archive_name = definitions_url.split('/')[-1]

    # Remove ".zip" to get base name
    base_name = archive_name[:-4]

    cache_dir = Path(CACHE)
    print(cache_dir.absolute())
    archive_path = cache_dir / archive_name
    zip_target_path = cache_dir / base_name
    cache_dir.mkdir(exist_ok=True)
    retrieve_archive(archive_path, definitions_url)
    unpack_archive(archive_path, zip_target_path)

    yield from zip_target_path.iterdir()


def unpack_archive(archive_path, zip_target_path):
    # Unpack spec
    print('Unpacking definitions...')
    with ZipFile(archive_path, 'r') as z:
        z.extractall(str(zip_target_path))
    print('Done.')


def retrieve_archive(archive_path, definitions_url):
    if not archive_path.exists():
        print('Downloading definitions...')
        request.urlretrieve(definitions_url, str(archive_path))
        print('Done.')


def upload_bundle(defs, base_url):
    entries = defs['entry']

    skipped = 0
    for entry in tqdm(entries):
        resource = entry['resource']
        resource_type = resource['resourceType']

        upload_resource(base_url, resource, resource_type)

    print(f'Finished uploading definitions. Skipped {skipped} resources')


def upload_resource(base_url, resource, resource_type):
    fhir_url = f'{base_url}/{resource_type}'
    response = requests.post(fhir_url, json=resource)
    if response.status_code not in OK_STATUS:
        print(response.status_code)
        print(response.content)
        print(resource)


if __name__ == '__main__':
    main()

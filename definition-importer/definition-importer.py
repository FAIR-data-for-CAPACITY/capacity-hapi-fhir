import json
from pathlib import Path
from urllib import request
from zipfile import ZipFile
import requests

import click

SPEC_DOWNLOAD_TEMPLATE = 'http://hl7.org/fhir/{fhir_version}/definitions.json.zip'
STU3 = 'STU3'
DEFINITIONS_ARCHIVE = 'definitions.zip'
DEFINITIONS = 'definitions'
JSON_EXTENSION = '.json'
CACHE = 'cache'

@click.command()
@click.option('--fhirversion', default=STU3, type=str)
@click.option('--baseurl', type=str)
def main(fhirversion, baseurl):
    # Download spec
    definitions_url = SPEC_DOWNLOAD_TEMPLATE.format(fhir_version=fhirversion)

    cache_dir = Path(CACHE)
    print(cache_dir.absolute())
    archive_path = cache_dir / DEFINITIONS_ARCHIVE
    zip_target_path = cache_dir / DEFINITIONS

    cache_dir.mkdir(exist_ok=True)

    if not archive_path.exists():
        print('Downloading definitions...')
        request.urlretrieve(definitions_url, str(archive_path))
        print('Done.')

    # Unpack spec
    print('Unpacking definitions...')
    with ZipFile(archive_path, 'r') as z:
        z.extractall(str(zip_target_path))

    # Upload valuesets
    valuesets_file = zip_target_path / 'valuesets.json'

    with valuesets_file.open('r') as valuesets_file:
        valuesets = json.load(valuesets_file)

        upload_definitions(valuesets, baseurl)


def upload_definitions(defs, base_url):
    entries = defs['entry']

    num_entries = len(entries)
    for idx, entry in enumerate(defs['entry']):
        resource = entry['resource']
        resource_type = resource['resourceType']

        fhir_url = f'{base_url}/{resource_type}'

        response = requests.post(fhir_url, json=resource)

        print(response.status_code)

        print(f'Uploaded {idx + 1} of {num_entries}')


if __name__ == '__main__':
    main()

#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=flats_ui.settings

FILE_NAME="result.json"
source venv/bin/activate

# run crawler
pushd scrapy
rm -f "${FILE_NAME}"
scrapy crawl trojmiasto -O "${FILE_NAME}"
BASE_PATH="$(pwd)"
FILE_PATH="${BASE_PATH}/${FILE_NAME}"
popd

# import data
pushd backend
python manage.py run_crawler --file "${FILE_PATH}"

popd

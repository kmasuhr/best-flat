#!/usr/bin/env sh

export DJANGO_SETTINGS_MODULE=flats_ui.settings

FILE_NAME="result.json"

DIR="venv"
if [ -d "$DIR" ]; then
  source venv/bin/activate
fi

# run crawler
cd scrapy
rm -f "${FILE_NAME}"
scrapy crawl trojmiasto -O "${FILE_NAME}"
BASE_PATH="$(pwd)"
FILE_PATH="${BASE_PATH}/${FILE_NAME}"
cd ..

# import data
cd backend
python manage.py run_crawler --file "${FILE_PATH}"
cd ..

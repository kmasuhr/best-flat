```shell
cd docker
docker compose up -d

# apply database migration
docker exec best-flat sh -c 'cd backend; python manage.py migrate'

# run trojmiasto.pl crawler
docker exec best-flat '/app/code/run-update.sh'

# open http://localhost:8000/list
```

![App](img.png)

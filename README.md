# docker-compose-MariaDB
docker-compose

Create .env
# MariaDB
MARIADB_ROOT_PASSWORD=root
MARIADB_DATABASE=testdb
MARIADB_USER=testuser
MARIADB_PASSWORD=testuserpassword
MARIADB_PORT=3036

# Run
docker compose -f docker-compose.yml -p my-mariadb up
docker compose -f docker-compose.yml -p my-mariadb logs -f
docker compose -f docker-compose.yml -p my-mariadb down



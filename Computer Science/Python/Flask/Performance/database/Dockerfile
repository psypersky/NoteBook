FROM postgres:10.0-alpine

# Copy necesary files from repository to docker volume and give them run permissions

ADD 1-setup-remote-connections.sh /docker-entrypoint-initdb.d/1-setup-remote-connections.sh
RUN chmod 755 /docker-entrypoint-initdb.d/1-setup-remote-connections.sh

ADD 2-create-database.sh /docker-entrypoint-initdb.d/2-create-database.sh
RUN chmod 755 /docker-entrypoint-initdb.d/2-create-database.sh

ADD 3-create-schema.sh /docker-entrypoint-initdb.d/3-create-schema.sh
RUN chmod 755 /docker-entrypoint-initdb.d/3-create-schema.sh
ADD schema.sql /usr
RUN chmod 755 /usr/schema.sql

ADD 4-add-fixed-data.sh /docker-entrypoint-initdb.d/4-add-fixed-data.sh
RUN chmod 755 /docker-entrypoint-initdb.d/4-add-fixed-data.sh
ADD fixed-data.sql /usr
RUN chmod 755 /usr/fixed-data.sql

# Add any step you want
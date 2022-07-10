
All *.sql files within the docker-entrypoint will be executed when you first run the container. 


1. Ensure your terminal is in this directory.
2. Run `docker build -t section2 .` (section2 is just the name can put anything you want)
3. Run `docker run -dp 5432 section2` (This runs your built container and now you can access the db at locahost:5432)
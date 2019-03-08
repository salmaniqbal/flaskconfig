### Flask App using config variables

This flask app includes connects to a mysql db. Both run in their own containers and can communicate via service name defined in `docker-compose.yml`.

In order to run this on your machine execute the following commands

`docker-compose build`  
`docker-compose up`

If you navigate to [http://localhost:5000](http://localhost:5000), you will see the app running which returns data from the mysql running in the container.

The db config variables are in the `config.json` & will be replaced by the build pipeline on build.

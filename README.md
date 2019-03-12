### Flask App using config variables

This flask app includes connects to a mysql db. Both run in their own containers and can communicate via service name defined in `docker-compose.yml`.

In order to run this on your machine execute the following commands

`docker-compose build`  
`docker-compose up`

If you navigate to [http://localhost:5000](http://localhost:5000), you will see the app running which returns data from the mysql running in the container.

The db config variables are in the `config.json` & will be replaced by the build pipeline on build.

----
#### Use config files for variables

`config.json` includes the variables that are to be used by the app. This should include credentials, secrets, urls etc. The secrets in the config file are to be replaced at build time. In case of Azure Build pipelines, the [Replace Tokens](https://marketplace.visualstudio.com/items?itemName=qetza.replacetokens) task can be used. This tasks looks for any place holder with a specified prefix and post fix and replaces it with the value stored in the build piplines.

In this projects case, `#{user}` & `#{password}` in the `config.json` are replaced.

In order to do this, follow the steps:

1. Update the code in your app to read the values from config file, take a look at `app.py` to see the whole code. Add the following code to read using configparser:  
```python
import configparser
with open('config.json', 'r') as f:
    config = json.load(f) 
```
Read the the values by using:

```python
user = config['DEFAULT']['USER']
password = config['DEFAULT']['PASSWORD']
```

2. Update the build definition to include replace token task and add the target to where the `config.json` file is:  
![Replace Token](./content/images/ReplaceToken.png)  In the same step under advanced option fill in the details for `Token prefix` & `Token suffix`. 

3. Under the pipeline variables, add the tokens that are to be replaced and their value. This way, secrets are not held in source control. They are in build pipeline.
![Secrets](./content/images/Secrets.png)


The better solution will be to put the secrets in [HashiCorp Vault](https://www.vaultproject.io/) or any other secret vault. 

---

#### Run Alembic Database upgrade scripts
If you would like to run Alembic upgrade scripts from your machine and your database is in Azure. You can modify the `alembic.ini` file to have the connection   

`sqlalchemy.url = mysql+pymysql://username:password@yourserver.database.azure.com/dbname`

`env.py` reads the connection string from `alembic.ini` file using:  
`url = config.get_main_option("sqlalchemy.url")`

You can change the url to get read the db `sqlalchemy.url` from `config.json` file instead
to read from the config file (have a look at app.py to see how this can be done)
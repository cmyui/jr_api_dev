# minimal jr. rest api dev expectations

this repo is a simple example of what i'd expect a dev coming into industry to be
able to work with.

while inevitably biased to my experience, i aim to be general in my expectations.

you're not expected to understand the inner clockwork of how all the parts fit
together - the key point is that you're able to work with the codebase.

you should have a general/layman's understanding of the following concepts:
1. git repositories, branches, pull requests, and commits
1. project structure (usecases, repositories, endpoints, services, settings)
1. basic http & rest semantics (methods, status codes, headers, body, query params)
1. relational (sql) databases, and migrations
1. virtual envrionments for dependency management
1. unit & integration test driven development
1. shell scripting (bash)
1. environmental variables

this project is a minimalistic user management rest api serving json content.

currently, it only implements two endpoints;
- `POST /users` - create a new user
- `GET /users/{user_id}` - fetch an existing user

with the skills described above, you should be able to ship new features
end-to-end, such as deleting users, updating users, or searching for users.

# setup
```sh
# create a virtual environment for the project's python dependencies
python3.9 -m virtualenv venv

# activate the virtual environment
source venv/bin/activate

# install the project dependencies
pip install -r requirements.txt

# create a configuration file & configure it
cp .env.example .env
nano .env

# start your mysql server
sudo service mysql start

# create the database
./scripts/create-db.sh

# start the server
./scripts/start.sh
```

# disclaimer

this code is intentionally made to be simple, and a real work environment will
(most likely) have much more of a complex codebase in inconsistent styles.

you're expected to understand the fundamentals of this project - but you should
expect to realistically be working in less ideal & consistent environments.

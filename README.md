# minimal jr. rest api dev expectations

this repo is a simple example of what i'd expect a dev coming into industry to
be able to work with. while inevitably biased to my experience, i aim to be
general in my expectations & advice.

don't worry about perfecting your understanding of the individual pieces - learn
enough of each piece to be able to use it's core features. understanding the
inner clockwork of how all the parts work under the hood will come with experience.

the key point is that you're able to work with the codebase, and are able to
build upon it to ship new features and ultimately deliver some value to the
end users of the api.

you should have a general/layman's understanding of the following concepts:
1. git repositories, branches, pull requests, and commits
1. project structure (usecases, repositories, endpoints, services, settings)
1. basic http & rest semantics (methods, status codes, headers, body, query params)
1. relational (sql) databases, and migrations
1. virtualization of software components through docker & docker-compose
1. virtual envrionments for dependency management
1. unit & integration test driven development
1. shell scripting (bash)
1. environmental variables

these are all standardized tools & concepts which allow us to more easily
develop our saas applications.

# the project

this is a stateless rest api serving json content over http/1.1.

currently, it only implements two endpoints;
- `POST /users` - create a new user
- `GET /users/{user_id}` - fetch an existing user

with the skills described above, you should be able to ship new features
end-to-end, such as deleting users, updating users, or searching for users.

a more advanced feature could be session management.

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

# build the api
make build

# start the api & backing services
make run
```

# disclaimer

this code is intentionally made to be simple & consistent to keep you focused on
building the application itself. a real work environment will (most likely) have
much more of a complex codebase, and likely not this level of consistency.

you're expected to understand the fundamentals of this project - but you should
expect to realistically be working in less ideal & consistent environments.

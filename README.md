## Flask Demo Project:

----

Project was created for a technical test, the requirements of the test were to the following:

1. Create a frontend application (in react) that will post data to
an API to be saved.
2. The API endpoint will have a gRPC service implemented that would
serve back to an external client data (upon request).

The inspiration behind this was to mimic a hackathon.
Best practises weren't taken into consideration, as time
was a limited factor.

### Setup:

----
Run the following commands
1. `cp .env.dist .env`
    - necessary to get a live copy of the environment files (change as appropriate)

2. `docker-compose build`
3. `python3 DBBootstrap.py`
    - Needed in order to bootstrap the db, need to have the correct tables in place
before trying to boot up the docker instances
4. `docker-compose up`
    - To boot up the docker instances

### gRPC integration:

----
The 'remote' client will actually be running on your local machine while the other 
services run on dockerized containers

Before being able to run the local, you'll need to install python3 requirements.
(You'll need pip for python 3, if on Ubuntu you can install it by running `sudo apt install python3-pip`)
Run the following to install the dependencies:
`pip3 install -r requirements.txt`

In order to query the backend to get information of saved data, run the following command:

`python3 GRPCClient.py <model id>`


### frontend Setup

---
Open `demopage.html` in your favourite browser.
Its not the expected react component of the project but due to
time limitations I was forced to keep things "simple".

 - Note, if you changed the port number of the flask service you'll
 need to make alterations to the url inside the `demopage.html` file.


# Address Book

A simple REST API to manage postal addresses, written in Python/Django.

**Table of Contents**

  * [Up and Running](#up-and-running)
  * [Available Endpoints](#available-endpoints)
  * [Notes, Assumptions](#notes-assumptions)
  * [License](#license)

## Up and Running

Assuming you have [Python 3](https://www.python.org/downloads/) installed, you have to follow the below steps to get the application running.

First, make sure to install the required dependencies via pip:

~~~~bash
pip install -r requirements.txt
~~~~

Then, set up the database:

~~~~bash
python manage.py migrate
~~~~

Optionally, add a user to the database:

~~~~bash
python manage.py createsuperuser
~~~~

Now you're all set to fire up the server:

~~~~bash
python manage.py runserver
~~~~

Rock 'n' Roll! :metal:

## Available Endpoints

The following endpoints are available:

  * Address
    * Create
    * Retrieve
    * Update and Partial Update
    * Delete and Batch Delete
    * List (filtered and paginated)
  * Token
    * Create Access and Refresh Token
    * Refresh Access Token
  * User
    * Get Current User

For details (such as request/response schemas), please refer to the OpenAPI documentation which is, by default, served at

  * http://127.0.0.1:8000/redoc

## Notes, Assumptions

Throughout the codebase you will find documentation comments detailing a few decisions (regarding the model, the URIs and such). Here I also provide notes and assumptions regarding things that might not have an exact codebase location.

### Assumption: Address vs Postal Address

In the requirements, one can mostly find the term "address". However, "postal address" also makes an appearance. Is there any difference between these two, or they refer to the same domain concept?

I assumed they are the same.

### Assumption: manage.py runserver

Since there was no need to deploy the code to a server, I assumed, it is enough that the application can be run via `manage.py runserver`.

### Assumption: Practical retrieval of multiple entries

The requirements stated that users shall be able to retrieve a larege number of addresses in a practical way. I assumed pagination is one such practical way. I used simple page-number pagination with a page size of 10. By adding pagination to the application, clients can retrieve multiple addresses without placing too much load on the server.

### Assumption: SQLite is fine

Since we're not deploying the application anywhere, I simply used SQLite. However, if we expect a large number of users and operations, of course, a standalone database backend would be necessary. Here, I opted for easy setup.

### Assumption: Token-based authentication is fine

As clients can hold state, and we are expecting a variety of clients, I thought token-based authentication is best because of its flexibility. From CLIs to mobile apps, token-based authentication work well. I did not implement logout, as I did not want to bother with token blacklisting :(

### Assumption: Default password constraints are fine

Usually, each site has its own constraints passwords must adhere to. In this case, I assumed, the default validation constraints are just fine.

### Note: Package-by-feature

Not sure if this is idiomatic Python/Django, but I used a package-by-feature approach to separate my Address and User endpoints.

## License

Address Book is available under [The MIT License](./LICENSE).

# Sojourner™

A personal blogging website where you can create and share your opinions and other users can read and comment on them.


## Installation
OS X

### Pre-requisites
* [Python 3.7.2](https://www.python.org/)
* IDE of your choice.


### Steps

* Clone the app to a directory.
```
git clone https://github.com/tc-mwangi/s-blog.git
```

* Install dependencies:

```
pip3 install -r requirements.txt
```


* Run program on terminal:

```
chmod a+x start.sh
```

* Run script:

```
./start.sh
```

### User Stories

* As a user, I would like to view the blog posts on the site.
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.


### BDD
|     | Behaviour    |          Input                  | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | register new user    | registration form data     | flash message of successful registration, redirect to login    |
|  2. |   authenticate user upon login |  login form data  | redirect to homepage, display user dashboard |
|  3. | display blog posts, latest first     | -     | -     |
|  4. | display random quotes| -   | quotes feed stream, refreshes on reloading page   |
|  5. | subscribe form call to action    | save email to database, append subscriber's list   | add email to subscribe list on confirmation, send subscription confirmation email.     |
|  6. |  author may delete offensive comments on comments stream  |  -  | delete all instances of the blog post |
|  7. | display edit blog form to update posted blogs | -   | update all instances of the post  |



## Author

**@top-cat** - *Initial work* - [Sojourner™](https://github.com/tc-mwangi/s-blog.git)


## Credits

**Quotes by** [-StormConsultancy]()

## License
MIT © [Sojourner™]()

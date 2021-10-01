# Colibri

## About
- A Twitter clone, but with RDBMS as schema defined in `Colibri. DBMS's 
- There are several Twitter clones, but each has a different DB Schema
  - Few examples can be found [here](https://stackoverflow.com/questions/11654420/) and [here](https://stackoverflow.com/questions/3745779/)
- TLDR; the solutions were using extra tables for every feature and storing the tweets and comment different tables
- Most of the previously mentioned DB models faced complications with Twitter features like
  - Retweets
  - Comment tweets
- So, what we could do?
  - Reverse architecture Twitter Links, 
    - on careful observation, it is obvious that every post on Twitter, whether an original tweet or retweet and comment all come under the same URL
      - So, behind the scenes, Twitter treats all the tweets as the same object 
      - This narrows the path of showing a single tweet model is used.
    - The other observation is, on retrieving a single tweet, all parents of that tweet are retrieved.
      - this shows, that Twitter is having some mapping to get parent tweets, (linked list)(hi DSA)
        - which is self joined to retrieve data
      - this appears all good, but there is another feature, retweets (Devil)
        - how could we do this, in general, tweeter shows who the original author is and when did current user retweeted
        - here, now we do something, little interesting, 
          - we would map the parent attribute to retweet to the original tweet same as how we map comments
        - but, how would we differentiate the retweets, original posts and comments 
          - so to classify this we have an ENUM object of three types `post`, `comment` and `retweet`
- This all appears good but how would be DB query look for retrieving history and generate a feed.
  - here comes something we don't across regularly (at least me) in ORMs and prod level code custom SQL functions 
  - we could write a custom SQL function of getting all records same as printing a linked list
  - a recursive function, until post type is either `post` or `retweet`. [here](https://stackoverflow.com/questions/1246725/)
  - generic way would be fetching DB until a post of type `retweet` or `post` appears but in this case, we are simply increasing the load, 
    - yes could use some limitation query and restricted such that the client needed a request for a parent.       

## Get Started
1. Clone the repo 
2. Create a virtual env
    ```
    python3 -m venv venv
    source ./venv/bin/activate 
    ```
3. Install Dependeince
    - pip
    ```
    pip install -r requirements.txt
    ```
4. Make Migrations
    - shell
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create Super User
    - shell
    ```shell
    python manage.py createsuperuser
    ```
5. Start Server
    - Django Server
    ```
    python manage.py runserver


## ToDo
- JWT for auth (Could you simple-JWT)

## Contribute 
- Client 
  - React App
    - Service
      - Auth Flow
    - Pages
      - Colibris
      - Users
- Server
  - Tests
  - Swagger

# Flask Keypoints 

A brief description of my takeaways from the course.

* In simple terms API is nothing but a program which takes some data and gives some other data back after processing it.

For example - In Twitter Search it accepts data(search parameters) and processes it(finds the tweets that matches the search parameters in the DB) and sends data back(in form of tweets).

* Code to create a basic Flask Application in python :
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

app.run(port=5006)
```

__Some of the doubts that I encountered in the above code__

*  `__name__` is used to uniquely identify our file which lets the Flask application to know that it is running on a unique location in the server.


* Since we never call the method in the code but it displays the text "Hello World!" as response to request which is made when the user visits URL http://127.0.0.1:5006/. This is because we have used a decorator `app.route` which maps the URL that the user requests to a function that performs some action. 

* Since we may have more than version of python installed in our system. To solve the problem we need to create a `virtual environment` and activate it and once it is activated, install flask and run the app :
```
python -m venv venv
.\venv\Scripts\activate
pip install flask
python app.py
```

* The `request` is what the user sends when visiting the URL http://127.0.0.1:5006/. The `response` is what the server sends back to the user after the request was received. The text we see in the browser is just part of a response.Both requests and responses have a standardized structure defined in the HTTP.


---

* What is a __web server__ ? <br>
-> It is a piece of software designed to accept incoming web requests.

* What do we send to a server when we enter the URL for a web page ? <br>
->  Let us take an example, https://www.twitter.com/login. 
In our case what the server sees is something like this :
```
GET/login/HTTP/1.1
(HTTP Verb->Path->Protocol along with version)
```

* When does the server produce error ?
    * If the path is not found
    * If the HTTP is not supported or some other protocol is supported like SMTP/FTP for email/file transfer purpose applications.
    * If the server is unavailable
    * It may give back some HTML Code/text or nothing if not configured.


* The `requests` are almost `identical` what users send. The difference lies on only `what the server responds with`.

---



__HTTP Verbs__

Verb | Meaning |
| :--- | ---:
GET     | Retrive something |
POST    | Receive data(creation) |
PUT     | Make sure something is there(updation)
DELETE  | Remove something

---

<br>

* __Some important clarifications on HTTP Verbs__

    * When you issue a HTTP request to authenticate a login which verb do you use ?

        * We use the POST verb because we are sending form data to the server (username and password)
        
    * What is the difference between  POST and PUT requests ?
        * POST and PUT are just pieces of data in a request.The only difference is what the receiving server decides to do with them once they reach it.
        * Normally applications will use POST to send data, and PUT to make sure some data is saved in the server.
        * For example, POST can be used to authenticate a user, and PUT to create a new item in a store.






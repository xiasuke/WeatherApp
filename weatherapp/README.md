# Build Instructions:
Make sure you are in the the weatherapp directory, where
you can see the app directory and run.py

1. If you do not have Python, go ahead and install it As well as `pip`.
2. Create virtual environment and install require packages

For Linux users:
```
$ pip install virtualenv
$ virtualenv flask
$ flask/bin/pip install flask
$ flask/bin/pip install flask-wtf
$ flask/bin/pip install requests
```

For Windows users:
```
$ pip install virtualenv
$ virtualenv flask
$ flask\Scripts\pip install flask
$ flask\Scripts\pip install flask-wtf
$ flask\Scripts\pip install requests
```

3. Get an api key from http://openweathermap.org/ and set the environment variable
`OWM_API_KEY` to your api key

4. Start the application

For Linux:
```
$ chmod a+x run.py
$ ./run.py
```

For Windows:
```
$ flask\Scripts\python run.py
```

4. Now you can test the application out in the browser:
```
http://localhost:5000
```
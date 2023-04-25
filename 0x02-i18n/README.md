 # i18n
---
i18n refers to the process of internationalizing Flask web applications. It is a support for Flask Application that is based on the Python [babel](https://babel.pocoo.org/en/latest/), [pytz](https://pythonhosted.org/pytz/) modules.

## Steps involved.
--- 
In Flask Babel, *i18n* involves the following steps:
* Marking strings in the application that need to be translated using the **`gettext`** function or its alias `_`.
* Extracting the marked strings into a message catalog using the **`pybabel extract`** command.
* Translating the message catalog into different languages using tools such as **`poedit` or `crowdin`**.
* Compiling the translated message catalog into binary .mo files using the **`pybabel compile`** command.
* Loading the appropriate translations for each user based on their language preference using the Flask Babel `Babel` extension.

## Installation
Install the extension from PyPi:
    `$ pip install Flask-Babel`
**N/B.**
Flask-Babel requires Jinja >=2.5.

## More Information:
* [Documentation](https://python-babel.github.io/flask-babel/)
* [GitHub](https://github.com/python-babel/flask-babel)
* [You Tube](https://www.youtube.com/watch?v=7Zfp2s1JBW)


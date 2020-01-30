# the door is closed

## The user can only open a website once. If it is exists in the browser history, then the site is blocked. Thus the name "The door is closed".

Transforming the chrome history into a csv file with a sqlite script.
This script ist being executed with a bash script.

With HTML and Template a website is being rendered. The inputed short url (google.com) is being concatenated to the rest of the hyperlink (https://www.). If the short link is existing in our .csv file the user will be redirected to the default page and get an error message else the hyperlink will be opened.

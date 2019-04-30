# MusicalSunburst
CS 205 Final Project
Contributors: Connor Allan, Jack Houk, Jake Liu, Shravya Suddala

---

For our final project in CS 205, we have choosen to create, design and implement a program that will display a music database in a graphical way on a web server. To accomplish this, we are utilizing [Django(2.1.7) as our framework](https://www.djangoproject.com/start/overview/) and [D3 Sunburst Charts](https://bl.ocks.org/vasturiano/12da9071095fbd4df434e60d52d2d58d) as our graphical display. The database will be hosted via the SQLite3 database that accompanies the Django framework.

https://think.cs.vt.edu/corgis/csv/music/music.html -- Derived datased based on previous option, appears to be more in line with our size constraints and our goals for content.

---

Setting up your local device to run the server!

1. Install Django 2.1.7 on your device! This should be done through a bash terminal, command: "pip install django" *NOTE: you will need to be running python 3.5+*

2. Install the required package: "pip install django_extensions"

3. Navigate to the root directory of the app, look for the manage.py file!

4. Run this command: "python manage.py runserver"

5. In your web browser go to: 127.0.0.1:8000/sunburst

That should allow you to run the server. If you have any questions about setting up the server to run locally on your device, please send any of us an email and we'll gladly help out!

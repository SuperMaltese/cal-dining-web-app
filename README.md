#cal-dining-web-app

Run dining_scraper.py. Make sure you have BeautifulSoup installed.

In terminal, type in APP_FLASK = server.py
flask run

Then, in a browser, go to 127.0.0.1:5000, or whichever ip address is returned by the above command.
In the browser url, append /$hall$/$meal$, where $hall$ is any selection of {Cafe_3, Foothill, Clark_Kerr_Campus, Crossroads}, and $meal$ is any selection of {Breakfast, Brunch, Lunch, Dinner}. Hit -> Enter.
  
The page should populate with the menu for the specific hall and meal type you specified for that day.

In Command Line
Type in Invoke-Restmethod $ip-address$/$hall$/$meal$
substituting in the correct values for each $$ place-holder.

How to run Splash
-----------------

Start Splash:

    docker-compose up -d

Stop Splash:

    docker-compose down --remove-orphans

How to run script
-----------------

Python 3 with `requests` is required.

Run script:

    python3 splash_avito_phone.py <url> -o output.png

Example URL: https://www.avito.ru/moskva/kvartiry/2-k_kvartira_84_m_412_et._992361048

It will create output png file `output.png`.

Expected result: mobile phone is displayed

Actual result: mobile phone is still hidden, as if button wasn't pressed.

Using Jupyter + Splash
----------------------

Another excellent way to debug Splash is by using Jupyter notebook to execute Lua code manually.

Run it via Docker:

    docker run -p 8888:8888 -it scrapinghub/splash-jupyter

Execute Lua code:

    splash:go("INSERT_URL_HERE")

    splash:runjs("document.getElementsByClassName('item-phone-button')[0].click()")
    splash:wait(2)
    splash:png()

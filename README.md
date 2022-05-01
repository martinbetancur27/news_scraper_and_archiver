# Vendor news scraper and archiver on yahoo news: Bloomberg, Reuters and many more. Skills: XPATH, Python, Selenium, Requests, Logic and POO

You have a list where you can select the Yahoo provider; the program will select the news, scrape it and save it locally.

Benefits::
=============

* Preserve information locally.
* Bloomberg is paid (here you have many free news).
* Reuters needs subscription to read (here you can read completely without subscription).
* You can filter by the provider you need or like.
* You do not see advertising, only the news in a txt file.
* Run only when you need to extract news.

Warnings:
=============
+ Do not resell or publish the news by other means. The information is not yours. Copyrighted news. Continually review robots.tex (https://finance.yahoo.com/robots.txt) to validate permissions. This program has the risk of becoming obsolete and can only be used for educational purposes or code reuse.

+ News beginning with the url /m/ are prohibited from scraping. I respect your decision and from the code I prevent taking this news. I encourage you to do the same. I leave the structure in case these news starts with another allowed structure or Yahoo decides to scrape them.

***I add the robots.txt to validate the permission***

    Some of these providers are Financial Times, Barrons.com, Investor's Business Daily, Market Watch

+ The scope of the program does not cover the provider's own pages. You can make use of the 'scraping_news_article.py' module to scrape the news page you need (the template receives the XPATH to scrape the title, time, author and body); The module also has a method to save the news.

+ The .gitignore has specified not to upload the news folders: (*-20*), it would cover the entire decade from 2020 to 2029.


Some providers to scrape:
-------------

![](https://data.bloomberglp.com/company/sites/51/2019/08/og-image-generic-lp.png)

![](https://marcas-logos.net/wp-content/uploads/2021/09/Thomson-Reuters-logo.png)

![](https://upload.wikimedia.org/wikipedia/commons/3/37/Yahoo_Finance_Logo_2019.png)

![](https://content.fortune.com/wp-content/uploads/2016/10/fortune-logo-2016-840x485.jpg)
About:

It's hard to say what exactly can make creative writing good. It's been said that varied sentence length makes for more interesting prose.

![](https://external-preview.redd.it/ApenTFXDKfJDSnQt1P_TAGC8ZHUjno4wPSv47_LCZn4.png?auto=webp&s=89fd7c96d14cd211d60ac23bd3b3e5218855e1aa)

* This program outputs several stats and graphs about the sentence lengths for plain text files.
* Several punctuation exceptions are handled:
    * abbreviations that end in periods such as Dr., A.M., and initials are ignored as ends of sentences
    * em dashes are ignored as extra words
    * titles, chapter headers, and page numbers are ignored in the sentence counts


Installation:
* pip install flask
* pip install plotly
* pip install pandas
* pip install PyPDF2


Current limitations:
* Certain cases like 1999-2007 should be handled as 2 words instead of 1.
* Certain formats of trailing ellipses are getting caught as sentences.
* .txt files don't retain text formatting like bold and italics.


Discoveries:
* Splitting sentences is a lot more complicated than at first glance, and that's not even getting into the pain of converting .rtf into .txt.


Tutorials and resources used:
* Flask Web Development with Python tutorial:
* * https://www.youtube.com/watch?v=ZVGwqnjOKjk&list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs

* Plotly, open source graphing library for Python
* * https://plot.ly/python/

* Pandas, data structure and analysis tools library for Python
* * https://pandas.pydata.org/pandas-docs/stable/index.html

* PyPDF2, PDF toolkit for Python
* * https://pypi.org/project/PyPDF2/

Tested with personal writing excerpts and officially released excerpts such as:
* Chapter 1 of Twilight by Stephenie Meyer: https://www.stepheniemeyer.co.uk/books/twilight/an-extract-from-twilight/
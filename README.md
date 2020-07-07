# hackernews-webcrawler
A simple webcrawler that prints a list of all the Articles on the first X Pages of hackernews with more than Y votes.

Inputs, in the form of sys.argv[1] and sys.argv[2], are X and Y respectively, where X is the number of pages (starting from Page 1) to be searched for News Articles.
Articles with more than or equal to Y votes will be displayed.

Display format:-

Title: (Title)
Link: (Link)
Votes: (Votes)

Simple program uses BeautifulSoup4 and Requests to get the HTML of the page and extract the useful information.

A practice project.

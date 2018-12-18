# yelp-scraper

Aspiring data scientist looking for interesting business trends, or an entrepreneur looking for potential business leads? yelp-scraper provides functionality to search through Yelp's databases to generate business data for your business needs.

This project was developed for the Bruin Digital Marketing team (BDM).

### Getting Started: 

This project was developed using Python 3.6 (https://www.python.org/). It uses the scrapy and pandas modules. Assuming you have a compatible version of Python running on your machine, set up the rest of the dependencies by running the following in your command module:

```
pip install scrapy
pip install pandas
```

You should be able to clone the GitHub repository and run yelp-scraper with no problems.

### Running the Scraper
The yelp-scraper takes two parameters: the business sector of interest, and the number of pages the yelp-scraper should crawl through. These parameters are passed into the scraper as follows. Keep in mind all parameters MUST be passed in as strings. The return data should be a .csv file containing business data.


```
 scrapy crawl business -a category=[Business Sector] -a nPages=[number of Pages]
```

For example, if I wanted information on the first three pages of dentists in Los Angeles, I would pass in this command:

```
 scrapy crawl business -a category="Dentists" -a nPages="3"
```

You may have to experiment with the category so that it matches the listing in Yelp's database.

### Future Improvements

Currently, the yelp-scraper has no functionality to specify geographic area, defaulting to the Greater Los Angeles Area. This improvement should be quite trivial to implement.

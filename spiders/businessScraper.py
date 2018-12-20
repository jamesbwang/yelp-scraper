
import scrapy
import pandas as pd


class bdmScraper(scrapy.Spider):
	name = "business"
	pageNum = 0
	inputKeys = {"name" : [],
				 "address" : [],
				 "website" : [],
				 "phone" : []}
	def start_requests(self):
		yield scrapy.Request('https://www.yelp.com/search?find_desc=' + self.category + '&find_loc=Los%20Angeles%2C%20CA&start=00')

	def parse(self, response):
		if(self.pageNum < int(self.nPages)):
			self.pageNum +=1
			for sel in response.xpath('//h3/a'):
				link = sel.xpath('@href').extract_first()
				self.logger.info('Name found! ' + sel.xpath('text()').extract_first())
				self.logger.info('Link found! ' + link)
				yield response.follow(link, callback=self.scrapeDeeper)
			nextPage = response.request.url[:-2] + str(self.pageNum*10)
			yield response.follow(nextPage, callback=self.parse)
		else:
			self.logger.info(str(self.inputKeys))
			df = pd.DataFrame.from_dict(self.inputKeys)
			df.to_csv(self.category + "_data.csv")

	def scrapeDeeper(self, response):
		address = response.css('div.mapbox-text address::text').extract_first()
		self.logger.info('address ' + address)
		phone = response.css('div.mapbox-text span.biz-phone::text').extract_first()
		self.logger.info('phone ' + phone)
		website = response.css('div.mapbox-text a::attr(href)').extract()[2]
		self.logger.info('website ' + response.urljoin(website))
		name = response.css('h1::text').extract_first()
		self.logger.info('name ' + name)
		self.inputKeys["name"] += [name.strip()]
		self.inputKeys["address"] += [address.strip()]
		self.inputKeys["website"] += [response.urljoin(website).strip()]
		self.inputKeys["phone"] += [phone.strip()]












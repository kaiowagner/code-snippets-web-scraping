# Scrapy

An open source and collaborative framework for extracting the data you need from websites.

## How to install Scrapy

```bash
pip3 install scrapy
```

## To run a spider
```bash
scrapy runspider hello_spider.py
```

## How to create a project
```bash
scrapy startproject courses
```

## How to create a spider within a project
```bash
scrapy genspider coursera 'coursera.org'
```

## How to run a spider within a project
```bash
scrapy crawl coursera
```

## How to use Scrapy Shell
```bash
scrapy shell https://www.coursera.org/browse?languages=pt
```
```python
divs = response.xpath('/html/body/ir-root/ir-content/ir-course-catalog-old/section/div/div/div/div[1]/div')
for div in divs:
    # if you know that xpath list has one element, then: extract_first() else extract()
    div.xpath('.//h3/a').extract_first()
```


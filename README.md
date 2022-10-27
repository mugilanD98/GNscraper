[![Contributors][contributors-shield]](https://img.shields.io/github/contributors/mugilanD98/GNscraper)
![PyPI - Downloads](https://img.shields.io/pypi/dm/GNscraper)
[![Forks][forks-shield]](https://github.com/mugilanD98/GNscraper/network/members)
![GitHub User's stars](https://img.shields.io/github/stars/mugilanD98?style=social)
[![Issues][issues-shield]](https://github.com/mugilanD98/GNscraper/issues)


<br />  
  
<h2>About GNscraper</h2>

  <p>
    GNscraper stands for Google News Scraper which scrape News Articles from Google News based on given Keywords and returns a Data Frame which contains Publishers, Title, Url, Uploaded Date and Uploaded DateTime of News Articles.
    <br />
    <br />
    <br />
    <br />
    ·
    <a href="https://github.com/mugilanD98/GNscraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/mugilanD98/GNscraper/issues">Request Feature</a>

  </p>

<!-- GETTING STARTED -->


### Installation

``` shell
pip install GNscraper
```

## Available Features

<br />  

* ### Get News by Keyword

<br />  
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20table%201.PNG" alt="GNscraper">
  </a>
<br />  

##### Example :


```python
from GNscraper import news_by_keyword

tesla_news = news_by_keyword('tesla')
tesla_news.head(10)
```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/master/img/key%20word.PNG" alt="GNscraper">
  </a>

<!-- USAGE EXAMPLES -->

<br />

* ### Available Countries

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/all%20available%20countries.PNG" alt="GNscraper">
  </a>

##### Example :
```python
from GNscraper import available_countries

countries = available_countries()
print(countries)
```
##### Output :
```
	country	             country_code
0	Australia	            AU
1	Botswana	            BW
2	Canada	                CA
3	Ethiopia	            ET
4	Ghana	                GH
5	India	                IN
6	Indonesia	            ID
7	Ireland	                IE
8	Israel	                IL
9	Kenya	                KE
10	Latvia	                LV
11	Malaysia	            MY
12	Namibia	                NA
13	New Zealand	            NZ
14	Nigeria	                NG
15	Pakistan	            PK
16	Philippines	            PH
17	Singapore	            SG
18	South Africa	        ZA
19	Tanzania	            TZ
20	Uganda	                UG
21	United Kingdom	        GB
22	United States	        US
23	Zimbabwe	            ZW
24	Czech Republic	        CZ
25	Germany	                DE
26	Austria	                AT
27	Switzerland	            CH
28	Argentina	            AR
29	Chile	                CL
30	Colombia	            CO
31	Cuba	                CU
32	Mexico	                MX
33	Peru	                PE
34	Venezuela	            VE
35	Belgium	                BE
36	France	                FR
37	Morocco	                MA
38	Senegal	                SN
39	Italy	                IT
40	Lithuania	            LT
41	Hungary	                HU
42	Netherlands	            NL
43	Norway	                NO
44	Poland	                PL
45	Brazil	                BR
46	Portugal	            PT
47	Romania	                RO
48	Slovakia	            SK
49	Slovenia	            SI
50	Sweden	                SE
51	Vietnam	                VN
52	Turkey	                TR
53	Greece	                GR
54	Bulgaria	            BG
55	Russia	                RU
56	Ukraine	                UA
57	Serbia	                RS
58	United Arab Emirates	AE
59	Saudi Arabia	        SA
60	Lebanon	                LB
61	Egypt	                EG
62	Bangladesh	            BD
63	Thailand	            TH
64	China	                CN
65	Taiwan	                TW
66	Hong Kong	            HK
67	Japan	                JP
68	Republic of Korea	    KR
```


* ### Available Languages

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/all%20available%20language.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import available_languages

languages = available_languages()
print(languages)
```
##### Output :

```
	language	       language_code
0	english	              en
1	indonesian	          id
2	czech	              cs
3	german	              de
4	spanish	              es-419
5	french	              fr
6	italian	              it
7	latvian	              lv
8	lithuanian	          lt
9	hungarian	          hu
10	dutch	              nl
11	norwegian	          no
12	polish	              pl
13	portuguese brasil	  pt-419
14	portuguese portugal	  pt-150
15	romanian	          ro
16	slovak	              sk
17	slovenian	          sl
18	swedish	              sv
19	vietnamese	          vi
20	turkish	              tr
21	greek	              el
22	bulgarian	          bg
23	russian	              ru
24	serbian	              sr
25	ukrainian	          uk
26	hebrew	              he
27	arabic	              ar
28	marathi	              mr
29	hindi	              hi
30	bengali	              bn
31	tamil	              ta
32	telugu	              te
33	malyalam	          ml
34	thai	              th
35	chinese simplified	  zh-Hans
36	chinese traditional	  zh-Hant
37	japanese	          ja
38	korean	              ko
```


* ### Available Date ranges

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/available%20date%20range.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import available_date_range

date_range = available_date_range()
print(date_range)
```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/daterange.PNG" alt="GNscraper">
  </a>


* ### Available Categories

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/available%20news%20categories.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import available_new_categories

news_categories = available_new_categories()
print(news_categories)
```
##### Output :

```
['Health',
 'Science',
 'Sports',
 'Entertainment',
 'Technology',
 'Business',
 'World',
 'National',
 'Top stories']
```


* ### Get News Articles in Specific Language Based on a Keyword 

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20and%20lang%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_keyword_lang

covid_df = news_by_keyword_lang('covid-19','ta')
covid_df.head(6)


```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20with%20%20lang.PNG" alt="GNscraper">
  </a>

* ### Get News Articles Based on Keyword within specific date_range
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20and%20date%20range%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_keyword_date

latest_tesla_df = news_by_keyword_date('tesla','1d')
latest_tesla_df.head(10)


```

##### Output :

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20date.PNG" alt="GNscraper">
  </a>


* ### Get News Articles Based on Keyword from specific Website

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20and%20web%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_keyword_web

BBC_tesla_df = news_by_keyword_web('tesla','www.BBC.com')
BBc_tesla_df.head(10)

```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/search%20bbc.PNG" alt="GNscraper">
  </a>


* ### Get News Articles based on location

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/location%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_loaction

chennai_news = news_by_loaction('channai')
chennai_news.head(10)


```

##### Output :

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/chennai.PNG" alt="GNscraper">
  </a>


* ### Get News Articles based on location in specific language
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/location%20lang%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_location_lang

chennai_news_df = news_by_location_lang('channai','te)
chennai_news_df.head(6)


```
##### Output :

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/chennai%2Cte.PNG" alt="GNscraper">
  </a>


* ### Get News Articles based on including and excluding keyword
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/include%20exclude%20table%202.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import news_by_keyword_exclude

tesla_df = news_by_keyword_exclude('tesla','Elon Musk')
tesla_df.head(6)


```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/tesla%20without%20elon.PNG" alt="GNscraper">
  </a>


* ### Get National headlines based on given Country Code and News Category

<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/news%20headlines%20table%201.PNG" alt="GNscraper">
  </a>

##### Example :

```python
from GNscraper import national_headlines_by_categories

IN_sports_df = national_headlines_by_categories('IN','Sports')
IN_sports_df.head(6)


```
##### Output :
<p align="center">
  <a href="https://github.com/mugilanD98/GNscraper">
    <img src="https://raw.githubusercontent.com/mugilanD98/GNscraper/main/img/sports%20india.PNG" alt="GNscraper">
  </a>





[contributors-shield]: https://img.shields.io/github/contributors/mugilanD98/GNscraper

[contributors-url]: https://github.com/mugilanD98/GNscraper/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/mugilanD98/GNscraper?style=social

[forks-url]: https://github.com/mugilanD98/GNscraper/network/members

[stars-shield]: https://img.shields.io/packagist/stars/mugilanD98/GNscraper

[stars-url]: https://github.com/mugilanD98/GNscraper/stargazers

[issues-shield]: https://img.shields.io/bitbucket/issues-raw/mugilanD98/GNscraper

[issues-url]: https://github.com/mugilanD98/GNscraper/issues


<br /> 
<br /> 
<br /> 
<br /> 
<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Mugilan Deiveegan - mugilan.deiveegan98@gmail.com







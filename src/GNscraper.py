import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
from datetime import date
from datetime import datetime



# country list
def available_countries():
    country={'Australia': 'AU', 'Botswana': 'BW', 'Canada ': 'CA', 'Ethiopia': 'ET', 'Ghana': 'GH', 'India ': 'IN',
     'Indonesia': 'ID', 'Ireland': 'IE', 'Israel ': 'IL', 'Kenya': 'KE', 'Latvia': 'LV', 'Malaysia': 'MY', 'Namibia': 'NA',
     'New Zealand': 'NZ', 'Nigeria': 'NG', 'Pakistan': 'PK', 'Philippines': 'PH', 'Singapore': 'SG', 'South Africa': 'ZA',
     'Tanzania': 'TZ', 'Uganda': 'UG', 'United Kingdom': 'GB', 'United States': 'US', 'Zimbabwe': 'ZW',
     'Czech Republic': 'CZ', 'Germany': 'DE', 'Austria': 'AT', 'Switzerland': 'CH', 'Argentina': 'AR', 'Chile': 'CL',
     'Colombia': 'CO', 'Cuba': 'CU', 'Mexico': 'MX', 'Peru': 'PE', 'Venezuela': 'VE', 'Belgium ': 'BE', 'France': 'FR',
     'Morocco': 'MA', 'Senegal': 'SN', 'Italy': 'IT', 'Lithuania': 'LT', 'Hungary': 'HU', 'Netherlands': 'NL',
     'Norway': 'NO', 'Poland': 'PL', 'Brazil': 'BR', 'Portugal': 'PT', 'Romania': 'RO', 'Slovakia': 'SK', 'Slovenia': 'SI',
     'Sweden': 'SE', 'Vietnam': 'VN', 'Turkey': 'TR', 'Greece': 'GR', 'Bulgaria': 'BG', 'Russia': 'RU', 'Ukraine ': 'UA',
     'Serbia': 'RS', 'United Arab Emirates': 'AE', 'Saudi Arabia': 'SA', 'Lebanon': 'LB', 'Egypt': 'EG',
     'Bangladesh': 'BD', 'Thailand': 'TH', 'China': 'CN', 'Taiwan': 'TW', 'Hong Kong': 'HK', 'Japan': 'JP',
     'Republic of Korea': 'KR'}
    country_list=pd.DataFrame(zip(country.keys(),country.values()),columns=['country','country_code'])
    return country_list



# language list
def available_languages():
    language={'english': 'en', 'indonesian': 'id', 'czech': 'cs', 'german': 'de', 'spanish': 'es-419', 'french': 'fr',
     'italian': 'it', 'latvian': 'lv', 'lithuanian': 'lt', 'hungarian': 'hu', 'dutch': 'nl', 'norwegian': 'no',
     'polish': 'pl', 'portuguese brasil': 'pt-419', 'portuguese portugal': 'pt-150', 'romanian': 'ro', 'slovak': 'sk',
     'slovenian': 'sl', 'swedish': 'sv', 'vietnamese': 'vi', 'turkish': 'tr', 'greek': 'el', 'bulgarian': 'bg',
     'russian': 'ru', 'serbian': 'sr', 'ukrainian': 'uk', 'hebrew': 'he', 'arabic': 'ar', 'marathi': 'mr', 'hindi': 'hi',
     'bengali': 'bn', 'tamil': 'ta', 'telugu': 'te', 'malyalam': 'ml', 'thai': 'th', 'chinese simplified': 'zh-Hans',
     'chinese traditional': 'zh-Hant', 'japanese': 'ja', 'korean': 'ko'}  
    language_list=pd.DataFrame(zip(language.keys(),language.values()),columns=['language','language_code'])
    return language_list    



# date range
def available_date_range():
    dateee={'1h':'news atricles from last hour','1d':'news from last 24 hours','7d':'news from last 7 days','1y':'news from last 12 months'}
    date_list=pd.DataFrame(zip(dateee.keys(),dateee.values()),columns=['date_range','date_range_description'])
    return date_list    



# news categories
def available_news_categories():
    tag_dict={'Health':-7,'Science':-8,'Sports':-9,'Entertainment':-10,'Technology':-11,'Business':-12,'World':-14,'National':-15,'Top stories':-18}
    return list(tag_dict.keys())




# only search term:
def news_by_keyword(search_term):
    search_term=search_term.replace(' ','%20')
    url='https://news.google.com/search?q='+search_term+'&hl=en-IN&gl=IN&ceid=IN%3Aen'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)      
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True)          
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data


# search term with language:
def news_by_keyword_lang(search_term,lang):
    search_term=search_term.replace(' ','%20')
    url='https://news.google.com/search?q='+search_term+'&hl='+lang+'-IN&gl=IN&ceid=IN%3A'+lang
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)                
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data


# news by location:
def news_by_loaction(location):
    location=location.replace(' ','%20')
    url='https://news.google.com/search?q='+location+'&hl=en-IN&gl=IN&ceid=IN%3Aen'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)      
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data


# news by location and language specified:
def  news_by_location_lang(location,lang):  # region may be city,state,country
    location=location.replace(' ','%20')
    url='https://news.google.com/search?q='+location+'&hl='+lang+'-IN&gl=IN&ceid=IN%3A'+lang
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)                
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data









# search term and exclude words:


def  news_by_keyword_exclude(search_term,exclude_words):
    search_term=search_term.replace(' ','%20')
    exclude_words=exclude_words.replace(' ','%20-')
    url='https://news.google.com/search?q='+search_term+'%20-'+exclude_words+'&hl=en-IN&gl=IN&ceid=IN%3Aen'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)                
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data



# search term and date range:


def  news_by_keyword_date(search_term,date_range):
    search_term=search_term.replace(' ','%20')
    url='https://news.google.com/search?q='+search_term+'%20when%3A'+date_range+'&hl=en-IN&gl=IN&ceid=IN%3Aen'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)                
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime'])
    return data



#must include .com or .in
def news_by_keyword_web(search_term,web):
    search_term=search_term.replace(' ','%20')
    web=web.replace(' ','')
    url='https://news.google.com/search?q='+search_term+'%20site%3A'+web+'&hl=en-IN&gl=IN&ceid=IN%3Aen'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')
    news_tag=soup.find_all(class_='ipQwMb ekueJc RD0gLb')
    
    news_list=[]
    for i in range(len(news_tag)):
        title=news_tag[i].text
        link='https://news.google.com/'+news_tag[i].a['href']
        title_link=[title,link]
        news_list.append(title_link)    
        
    date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
    date_list=[] 
    for j in range(len(date_tag)): 
        datee=date_tag[j]['datetime']
        date_text=date_tag[j].text
        date_datetext=[datee,date_text]
        date_list.append(date_datetext)        
        
        
    source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
    source_list=[]
    for k in range(len(source_tag)):
        source=source_tag[k].text
        source_list.append(source)   
        
    if len(source_list) > 0:    
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        data=pd.DataFrame(columns=['publisher','Title', 'Link', 'Date_in_Text','uploaded_date', 'uploaded_datetime'])        
    return data    



def national_headlines_by_categories(region,category):
    if category == 'National':
        category='Country'
    else:
        category=category
        
        
    tag_dict={'Health':-7,'Science':-8,'Sports':-9,'Entertainment':-10,'Technology':-11,'Business':-12,'World':-14,'Country':-15,'Top stories':-18}
    url='https://news.google.com/topstories?hl=en-'+region+'&gl='+region+'&ceid='+region+':en'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'lxml')    
    if tag_dict[category] == -18:  
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]       
    elif tag_dict[category] == -7:
        url='https://news.google.com/'+soup.find_all('a')[-7]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]    

    elif tag_dict[category] == -8:
        url='https://news.google.com/'+soup.find_all('a')[-8]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]         
        
    elif tag_dict[category] == -9:
        url='https://news.google.com/'+soup.find_all('a')[-9]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]    
        
    elif tag_dict[category] == -10:
        url='https://news.google.com/'+soup.find_all('a')[-10]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]    
        
    elif tag_dict[category] == -11:
        url='https://news.google.com/'+soup.find_all('a')[-11]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]            
        
    elif tag_dict[category] == -12:
        url='https://news.google.com/'+soup.find_all('a')[-12]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]         
        
        
    elif tag_dict[category] == -14:
        url='https://news.google.com/'+soup.find_all('a')[-14]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]  
        
    elif tag_dict[category] == -15:
        url='https://news.google.com/'+soup.find_all('a')[-15]['href']
        r = requests.get(url)
        coverpage = r.content
        soup = BeautifulSoup(coverpage, 'lxml') 
        us_news_tag=soup.find_all(class_='DY5T1d RZIKme')
        news_list=[]
        for i in range(len(us_news_tag)):
            title=us_news_tag[i].text
            link='https://news.google.com/'+us_news_tag[i]['href']
            title_link=[title,link]
            news_list.append(title_link)    

        date_tag=soup.find_all(class_='WW6dff uQIVzc Sksgp slhocf')
        date_list=[] 
        for j in range(len(date_tag)): 
            datee=date_tag[j]['datetime']
            date_text=date_tag[j].text
            date_datetext=[datee,date_text]
            date_list.append(date_datetext)        


        source_tag=soup.find_all(class_='wEwyrc AVN2gc uQIVzc Sksgp slhocf')
        source_list=[]
        for k in range(len(source_tag)):
            source=source_tag[k].text
            source_list.append(source)                
        data=pd.DataFrame(news_list,columns=['Title','Link'])
        data[['Date','Date_in_Text']]=date_list
        data['publisher']=source_list   
        data['uploaded_date']=pd.to_datetime(data['Date']).dt.date
        data['uploaded_datetime']=data['Date'].astype('datetime64[ns]')
        data=data.sort_values('uploaded_datetime',ascending=False)
        data = data.reset_index(drop=True) 
        data=data[['publisher','Title', 'Link','uploaded_date', 'uploaded_datetime']]
    else:
        aaaa=0
    return data    
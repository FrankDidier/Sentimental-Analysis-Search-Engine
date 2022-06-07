
from search_engine_app.models import UserPortal
from django.contrib.auth.models import User
#from search_engine_app.tasks import CheckEevent

""" This file is to implement observer pattern
@Author: Adarsh Koppa Manjunath"""



class NewsPublisher:
   def __init__(self):
       """Declare private list of authenicated and subscribed users"""
       self.notify_dict={}
       self._db_authenticated_users=User.objects.all()
       self._db_subscribed_users=UserPortal.objects.all()
       self._authenticated_users=[index.username for index in self._db_authenticated_users ]
       self._subscribed_users= [index.username for index in self._db_subscribed_users]

   def add_newsreader(self, news_reader_username,topic,sentiment):
       """add newsreader's topic and sentiment to the database"""
       
       print(self._db_subscribed_users)
       if str(news_reader_username) in self._subscribed_users:
           for news_reader in self._db_subscribed_users:

               if news_reader.username==str(news_reader_username):
                    
                    if news_reader.topic!=topic or news_reader.sentiment!=sentiment:
                        news_reader.topic=topic
                        news_reader.sentiment=sentiment
                        news_reader.save(update_fields=['topic','sentiment'])
                        return "topic or sentiment is updated"
       else:
           
           if  str(news_reader_username) in self._authenticated_users:
               newsreader=UserPortal(username=str(news_reader_username),topic=topic,urls="",updatedate="",sentiment=sentiment)        
               newsreader.save()
               return " topic and sentiment is entered"

   def remove_newsreader(self, username):
       """remove subscribed users from database"""
       userportal.objects.filter(username=news_reader_username).delete()
       return "user is removed"

   def notify(self,username):
       
    
        result={}
        from datetime import date
        for news_reader in self._db_subscribed_users:
                
            if news_reader.username==str(username):
                url_list=news_reader.urls.strip("][").split(',')
                urls=[]
               
                for index in url_list:
                    urls.append(index.strip(" '"))
                    
                news_reader.urls=urls
    
                result={ 'topic': news_reader.topic, 'url' :news_reader.urls, 'sentiment': news_reader.sentiment, 'date': date.today()}
                
                return result
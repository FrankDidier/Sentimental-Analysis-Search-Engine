from background_task import background
from django.contrib.auth.models import User
from search_engine_app.models import UserPortal
from search_engine_app.search_web import SearchWeb
from search_engine_app.observer_pattern.subject_topic import NewsPublisher

"""This file is to monitor url status, back-ground task linrary is used for this task.
"""




class CheckUpdate(NewsPublisher):

        
                


        @background(schedule=10)
        def monitor_urls_status():
                # lookup user by id and send them a message
                
                notifobj=NewsPublisher()
        
                db=UserPortal.objects.all()
                
                
                for index in db:
                        topic=index.topic
                        serach_obj=SearchWeb(topic,sentiment=index.sentiment,num=3, stop=3, final_output={},sentiment_dict={})
                        search_result=serach_obj.thread_func()
                        url_list=search_result.keys()
                
                        if index.urls == str(list(url_list)):
                                notifobj.notify_dict[index.username]=False
                        else: 
                                index.urls=str(list(url_list))
                                index.save(update_fields=['urls'])
                                notifobj.notify_dict[index.username]=str(list(url_list))
                print(notifobj.notify_dict)
        
                return notifobj.notify_dict        

publisher_obj=CheckUpdate()
change=publisher_obj.monitor_urls_status(repeat=50)


        

from search_engine_app.views.import_required_view_libraries import *


class UserPortalView(View):
    


    def userPortal(request):
        if request.method=="POST":
                
                form3 = userPortalForms(request.POST)

                if form3.is_valid():
                    topic = form3.cleaned_data['topic']
                    sentiment = form3.cleaned_data['options']
                    subject=NewsPublisher()
                    status=subject.add_newsreader(request.user,topic,sentiment)
                
                
                    messages.success(request, status)
            
                
        form3 = userPortalForms()
            
            
        return render(request,"userPortal.html",{'form': form3}) 
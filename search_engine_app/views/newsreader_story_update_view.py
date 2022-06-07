from search_engine_app.views.import_required_view_libraries import *

class NewsReaderStoryUpdateView(View):
    def __init__(self):
        self._userstatedict={}
        self._dbuserportal=UserPortal.objects.all()
        for index in self._dbuserportal:
             self._userstatedict[index.username]=index.urls

    def viewYourUpdatedResult(request):
        subjobj=NewsPublisher()
        result=subjobj.notify(request.user)
        result={'result':result}
        return render(request, 'viewYourUpdatedResults.html', result)
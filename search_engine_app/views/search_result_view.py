from search_engine_app.views.import_required_view_libraries import *

class SearchResultView(View):

    def search(request):
        """This function communicates between template and search_web files"""
        try:
            if request.method=="POST":
                
                form = GeneralForms(request.POST)

                if form.is_valid():
                    topic=form.cleaned_data['name']
                    sentiment = form.cleaned_data['options']
                    search_web_obj=SearchWeb(topic,final_output={},sentiment=sentiment,sentiment_dict={})
                    result=search_web_obj.thread_func()

                    if type(result)==str:
                        args = {'result': result}

                        return render(request, "alert.html", args)
                    else:
                        args = {'result':result,'sentiment':sentiment}
                        return render(request,"results.html", args)


            form = GeneralForms()
            
            
            return render(request,"home.html",{'form': form}) 


        except Exception as e:
            log.error('An exception occurred: {}'.format(e))
            log.error(traceback.format_exc())
from search_engine_app.views.import_required_view_libraries import *

class FeedbackView(View):

    def feedback_view(request):
        
        if str(request.user)=='AnonymousUser' or request.user==None or request.user=="":
            #messages.error(request,'Logine Required!!')
            return HttpResponse("<html> <body> <a href=""feedback_login.html"">Login Required</a>  </body></html>")
        else:
            
            if request.method=="POST":
                form = feedBackForm(request.POST)

                if form.is_valid():
                    subject=form.cleaned_data['subject']
                    email = form.cleaned_data['email']
                    message = form.cleaned_data['message']
                    #messages.success(request, 'Thankyou for giving all the information, we will get back to you shortly!!!')
                    feedobj=Feedback(username=str(request.user), user_email=str(email), subject=str(subject), feedback=str(message))
                    feedobj.save()
                    form = GeneralForms()
                    return HttpResponse("<html> <body> <a href=""home.html"">Thanks for the feedback! Continute to browse</a>  </body></html>")

            form = feedBackForm()
            return render(request,"feedBack.html",{'form': form})
           




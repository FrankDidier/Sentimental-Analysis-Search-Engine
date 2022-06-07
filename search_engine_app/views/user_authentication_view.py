from search_engine_app.views.import_required_view_libraries import *
 
class UsersAuthenticationView(View):

    def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                uname = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ uname )
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

    def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password )
            if user is not None:
                login(request, user)
                print(request.path)
                return redirect('userPortal.html')
            else:
                messages.error(request,'Login failed!!! invalid credentials.')
        context = {}
        return render(request, 'login.html', context)

    def logoutUser(request):
        logout(request)
        return redirect('login')

    def feedback_login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password )
            if user is not None:
                login(request, user)
                print(request.path)
                return redirect('feedBack.html')
            else:
                messages.error(request,'Login failed!!! invalid credentials.')
        context = {}
        return render(request, 'login.html', context)
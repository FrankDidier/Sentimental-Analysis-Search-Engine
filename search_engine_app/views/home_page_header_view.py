from search_engine_app.views.import_required_view_libraries import *


class HomePageIntroView(View):
    def ise(request):
        return render(request, "ise.html")

    def projectTeam(request):
        return render(request, "projectTeam.html")

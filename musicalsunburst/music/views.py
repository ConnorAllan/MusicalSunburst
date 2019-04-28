from django.shortcuts import get_object_or_404, get_list_or_404, render

from sunburst.models import Releases

# Create your views here.

def index(request):
    ## Pulls releases table from the database
    releases_list = Releases.objects.all()
##    releases_list = get_list_or_404(Releases)

    ## passes the list of objects into a contex meaning
    context = {'releases_list': releases_list}

    ## Draws them in the browser, mixing the index.html with the list of Releases
    return render(request, 'music/index.html', context)

def detail(request, release_id):
    ## Generates a check for a 404 error
    release = get_object_or_404(Releases, pk=release_id)

    ## Either draws a 404 error or brings user to details page about the release
    return render(request, 'music/detail.html', {'release': release})

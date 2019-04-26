from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    all_releases=Releases.objects.all()
    context={
        'all_albums' : all_releases,
    }
    return render(request,'music/index.html',context)


def detail(request,release_id):
    release = get_object_or_404(Album,pk=pmkRelease)
    return render(request,'music/detail.html',context)

def favorite(request,release_id):
    releases=Releases.objects.get(pk=pmkRelease)
    try:
        sectected_song=release.song_set.get(pk=request.POST['song'])
    except (KeyError , Song.DoesNotExist):
        return render(request , 'music/detail.html',{
            'release':release,
            'error_message':"Invalid option",
            })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',context)

def UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #now the user when submits form its post request not get request so now we will be dealing with it here
    #give blank
    def get(self,request):
        form=self.form_class(None)
        return render(request , self.template_name,{'form':form})

    #now if post then needed to be stores in the database
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #we we cheak the data from the user and then we weill add the data
            user = form.save(commit = False)

            #cleaned formatted (Normalise) data like many would have used DuDeCOol ike things so normalise

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Now how to change the password since they are not plane text
            user.set_password(password)
            user.save()#save it to database

            #now the authentication and logging the User
            user = authenticate(username=username , password=password)

            if user is not None:

                if user.is_active:

                    login(request,user)

                    #now redirecting them to the hompage of their app
                    return redirect('music:index')

        return render(request,self.template_name, {'form':form})


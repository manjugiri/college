from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'insideapex/about_us.html')

    # return HttpResponse("this is about[age")

def acs(request):
    return render(request, 'insideapex/apex-carrer-service.html')

def globalconnection(request):
    return render(request, 'insideapex/global-connection.html')

def student(request):
    return render(request, 'insideapex/student-experience.html')



# academics

def bcis_syllabus(request):
    return render(request, 'academics/BCIS.html')


def bba_syllabus(request):
    return render(request, 'academics/BBA.html')

def bba_bi_syllabus(request):
    return render(request, 'academics/BBA-BI.html')

def bba_tt_syllabus(request):
    return render(request, 'academics/BBA-TT.html')

def mba_syllabus(request):
    return render(request, 'academics/MBA.html')

def mba_evening_syllabus(request):
    return render(request, 'academics/MBA-Evening.html')


def online_councelling(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        previouscollege = request.POST.get('previouscollege')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        program = request.POST.get('program')
        Onlinecouncelling = Contact(firstname=firstname, lastname=lastname, address=address,
         previouscollege=previouscollege, email=email, contact_no=contact_no, program=program)
        Onlinecouncelling.save()

    return render(request, 'online_councelling.html')

def newsandnotices(request):
    return render(request, 'newsandnotices.html')

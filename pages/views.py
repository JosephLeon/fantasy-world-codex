from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to Fantasy World Codex!')


def detail(request, character_id):
    return HttpResponse("Behold! this is the page of %s" % character_id)


def results(request, character_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % character_id)


# def region(request, region_id):
#     return HttpResponse("The region is %s." % region_id)

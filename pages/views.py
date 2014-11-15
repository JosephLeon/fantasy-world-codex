from django.http import HttpResponse
from django.template import RequestContext, loader
from pages.models import Region


def index(request):
    region_list = Region.objects.all()
    template = loader.get_template('pages/index.html')
    context = RequestContext(request, {
        'region_list': region_list,
    })
    return HttpResponse(template.render(context))
    # output = ', '.join([p.region_name for p in region_list])
    # return HttpResponse(output)


def detail(request, character_id):
    return HttpResponse("Behold! this is the page of %s" % character_id)


def results(request, character_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % character_id)


def region(request, region_id):
    return HttpResponse("The region is %s." % region_id)

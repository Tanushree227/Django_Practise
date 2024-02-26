from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mypeoples = Member.objects.all().values()
  template = loader.get_template('peoples.html')
  context = {
    'mypeoples': mypeoples,
  }
  return HttpResponse(template.render(context, request))
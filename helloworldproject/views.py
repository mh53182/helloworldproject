from pathlib import Path
from django.http import HttpResponse
from django.views.generic import TemplateView

# urls.pyからリクエストオブジェクトを受け取るために引数が必要
# 今回はrequestとなっているが任意の引数名でOK
def helloworldfunction(request):
    returned_object = HttpResponse('<h1>Hello World</h1>')
    return returned_object

# Lesson114 補足：BASE_DIR
def someview(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse('aaaaa')

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
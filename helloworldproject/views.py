from django.http import HttpResponse

# urls.pyからリクエストオブジェクトを受け取るために引数が必要
# 今回はrequestとなっているが任意の引数名でOK
def helloworldfunction(request):
    returned_object = HttpResponse('<h1>Hello World</h1>')
    return returned_object
    
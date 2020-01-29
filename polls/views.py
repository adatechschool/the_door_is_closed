from django.shortcuts import render
from django.http import HttpResponse



class Handle:
    def __init__(self, req):
        self.req = req
        return

    def get_br_page(self):
        open_html = "browser.html"
        main_page = render(self.req, open_html)
        return main_page

    def check(self):
        blocking_site = self.req.POST.get("site")
        print(blocking_site)
        return

def print_submit(request):
    return HttpResponse("Ayyyyyyyy lmao.")

def index(request):
    hdl = Handle(request)
    hdl.check()
    out = hdl.get_br_page()
    return out

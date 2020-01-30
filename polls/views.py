from django.shortcuts import render
from django.http import HttpResponse
import os, csv
# from models import Handle

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
        print(type(blocking_site))
        with open("read_history/data.csv", "r") as hist_dat:
            hist_dat_read = csv.reader(hist_dat, delimiter=",")
            for url_line in hist_dat_read:
                if blocking_site in url_line[1]:
                    print(blocking_site)
                pass
        return None


def redirect(request):
    return HttpResponse("Ayyyyyyyy lmao.")

def index(request):
    hdl = Handle(request)
    out = hdl.get_br_page()
    return out

def redirect_site(request):
    # hdl.check()
    return

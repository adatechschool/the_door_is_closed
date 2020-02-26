from django.shortcuts import render
from django.http import HttpResponse
import os, csv, webbrowser


class Handle:
    def __init__(self):
        self.blocking_site = self.req.POST.get("site")
        return

    def check(self):
        print(self.blocking_site)
        if type(self.blocking_site) != str:
            return "wrong"
        with open("read_history/data.csv", "a+") as hist_dat:
            hist_dat_read = csv.reader(hist_dat, delimiter=",")
            for url_line in hist_dat_read:
                if self.blocking_site in url_line[1]:
                    return "blocked"
        return "go_ahead"

    def site_cond(self):
        check_result = self.check()
        redirect_to = ["browser.html"]
        if check_result == "wrong":
            open_choice = redirect_to[0]
        elif check_result == "blocked":
            open_choice = redirect_to[0]
        elif check_result == "go_ahead":
            webbrowser.open(self.blocking_site)
            open_choice = redirect_to[0]
        return main_page

hdl = Handle()
hdl.site_cond()

def index(request):
    return render(request, "browser.html")

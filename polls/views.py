from django.shortcuts import render
from django.http import HttpResponse
import os, csv, webbrowser


class Handle:
    def __init__(self, req):
        self.req = req
        return

    def check(self):
        blocking_site = self.req.POST.get("site")
        if type(blocking_site) != str:
            return "wrong"
        with open("read_history/data.csv", "r") as hist_dat:
            hist_dat_read = csv.reader(hist_dat, delimiter=",")
            for url_line in hist_dat_read:
                if blocking_site in url_line[1]:
                    return "blocked"
        return "go_ahead"

    def valid_link(self):
        return

    def site_cond(self):
        check_result = self.check()
        redirect_to = ["browser.html"]
        if check_result == "wrong":
            open_choice = redirect_to[0]
        elif check_result == "blocked":
            open_choice = redirect_to[0]
        elif check_result == "go_ahead":
            webbrowser.open('https://stackoverflow.com')
            open_choice = redirect_to[0]
        main_page = render(self.req, open_choice)
        return main_page


def index(request):
    hdl = Handle(request)
    main_out = hdl.site_cond()
    return main_out

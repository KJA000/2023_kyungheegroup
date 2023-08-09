from django.shortcuts import render

def mainpage(request):
 context = {'active_page': 'home'}
 return render(request, 'pages/mainpage.html',context)
def company(request):
 context = {'active_page': 'company'}
 return render(request, 'pages/company_info.html',context)

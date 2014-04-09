from django.views import generic

class WelcomeView(generic.TemplateView):
    template_name = 'checkunits/welcome.html'

class AboutUsView(generic.TemplateView):
    template_name =  'checkunits/aboutus.html'

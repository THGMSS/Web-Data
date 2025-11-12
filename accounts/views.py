from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        access_mode = self.request.POST.get('access_mode')
        if access_mode == 'admin':
            return reverse_lazy('admin:index')
        return super().get_success_url()
        
def login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    return redirect('/home/')
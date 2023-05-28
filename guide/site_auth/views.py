
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('main') 
    redirect_authenticated_user = True
    def form_invalid(self, form):
        """
        Called when the submitted form is invalid.
        Logs the errors and adds a flash message for each error.
        """
        logger.error('Login form is invalid')
        for field_name, errors in form.errors.items():
            for error in errors:
                logger.error(f'Error in {field_name}: {error}')
                messages.error(self.request, f'Error in {field_name}: {error}')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Log in')
        return context


class CustomUserRegistrationView(CreateView):
    template_name = 'auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    
    extra_context = {'title': 'Register', 'form': form_class}
    def form_valid(self, form):
        # Save the form data
        response = super().form_valid(form)
        
        # Process the uploaded file
        file = form.cleaned_data.get('file')
        if file:
            # Update the user model with the file information
            user = form.instance
            user.photo = file
            user.save()
        
        return response
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main')
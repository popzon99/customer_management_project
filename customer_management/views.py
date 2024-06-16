from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomerForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer, CustomerStatus

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'customer_management/register.html'
    success_url = reverse_lazy('maker_dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('maker_dashboard' if self.request.user.role == 'maker' else 'checker_dashboard')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class MakerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'customer_management/maker_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_filter = self.request.GET.get('status')
        customers = Customer.objects.filter(maker=self.request.user)
        if status_filter:
            customers = customers.filter(status__status=status_filter)
        context['customers'] = customers
        context['status_filter'] = status_filter
        context['user'] = self.request.user
        return context

class CheckerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'customer_management/checker_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_filter = self.request.GET.get('status')
        customers = Customer.objects.filter(maker__assigned_checker=self.request.user)
        if status_filter:
            customers = customers.filter(status__status=status_filter)
        context['customers'] = customers.select_related('maker')
        context['status_filter'] = status_filter
        context['user'] = self.request.user
        return context


class UploadCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_management/upload_customer.html'
    success_url = reverse_lazy('maker_dashboard')

    def form_valid(self, form):
        form.instance.maker = self.request.user
        response = super().form_valid(form)
        CustomerStatus.objects.create(customer=self.object, checker=self.request.user.assigned_checker)
        return response

class EditCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_management/edit_customer.html'
    success_url = reverse_lazy('maker_dashboard')

    def get_queryset(self):
        return Customer.objects.filter(maker=self.request.user)

class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = CustomerStatus
    fields = ['status']
    template_name = 'customer_management/update_status.html'
    success_url = reverse_lazy('checker_dashboard')

    def get_object(self, queryset=None):
        customer = get_object_or_404(Customer, id=self.kwargs['customer_id'], maker__assigned_checker=self.request.user)
        return customer.status

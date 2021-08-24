from django.shortcuts import render

# Create your views here.
from .models import Item

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_items = Item.objects.all().count()
    buyer_list = Item.objects.values('buyer')

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_items': num_items,
        'num_visits': num_visits,
        'buyer_list': buyer_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

from django.contrib.auth.mixins import PermissionRequiredMixin

class ItemListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'shoppinglist.can_read_all_item'
    model = Item
    paginate_by = 10

from django.contrib.auth.mixins import LoginRequiredMixin

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item

class ItemByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing items for current user (as buyer)."""
    model = Item
    template_name ='shoppinglist/buyer_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Item.objects.filter(buyer=self.request.user).order_by('title')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from shoppinglist.forms import CreateItemForm

def ItemCreateDIY(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateItemForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)

            data = Item(title = form.cleaned_data['title'] ,amount = form.cleaned_data['amount'], summary = form.cleaned_data['summary'], buyer = request.user)
            data.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('my-shopping-list') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateItemForm(initial={'title': '' ,'amount': '', 'summary': ''})

    context = {
        'form': form,
    }

    return render(request, 'shoppinglist/create_item.html', context)

##class ItemCreate(CreateView):
##    model = Item
##    fields = ['title', 'amount', 'summary',]
##    initial = {'amount': '1'}

class ItemUpdate(UpdateView):
    model = Item
    fields = ['title', 'amount', 'summary',]
    initial = {'amount': '1'}

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('my-shopping-list')
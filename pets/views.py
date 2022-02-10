from distutils.command.build_scripts import first_line_re
from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .forms import PetForm, CustomerForm


from .models import Pet, Customer

# Create your views here.
class IndexView(ListView):
    model = Pet
    context_object_name = 'pet_list'
    template_name = "pets/index.html"


class DetailView(View):

    # need to understand this function better, why is super(DetailView).dispatch required even for gets
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(DetailView, self).dispatch(*args, **kwargs)

    def get(self, request, pet_id):
        pet_info = Pet.objects.get(pk=pet_id)
        form = CustomerForm
        context = {'info': pet_info, 'form': form}
        return render(request, 'pets/detail.html', context)

    def post(self, request, pet_id):
        # changes pet to sold
        pet = get_object_or_404(Pet, pk=pet_id)
        pet.sold = True
        pet.save()
        # creates new customer
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/pets/{pet_id}')

    def delete(self, request, pet_id):
        pet = get_object_or_404(Pet, pk=pet_id)
        pet.delete()
        return redirect('/pets')


def add_pet(request):
    submitted = False
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pets/add_pet?submitted=True')
    else:
        form = PetForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "pets/addPet.html", {'form': form, 'submitted': submitted})


def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        pets = Pet.objects.filter(category__contains=searched)

        return render(request, "pets/index.html", {'pet_list': pets})


# old code before refactors
# @csrf_exempt
# def index(request):
#     first_four_pets = Pet.objects.all()[:4]
#     context = {'pet_list': first_four_pets}
#     return render(request, 'pets/index.html', context)


# class IndexView(View):
#     def get(self, request):
#         first_four_pets = Pet.objects.all()[:4]
#         context = {'pet_list': first_four_pets}
#         return render(request, 'pets/index.html', context)


# @csrf_exempt
# def detail(request, pet_id):
#     pet_info = Pet.objects.get(pk=pet_id)
#     context = {'info': pet_info}
#     return render(request, 'pets/detail.html', context)


# class AddPetView(View):
#     def get(self, request):
#         return render(request, 'pets/addPet.html', )

#     def post(self, request):
#         new_pet = Pet(
#             name=request.POST['name'],
#             breed=request.POST['breed'],
#             age=request.POST['age'],
#             color=request.POST['color'],
#             category=request.POST['category'],
#             description=request.POST['description'],
#             imageUrl=request.POST['imageUrl'],
#         )
#         new_pet.save()
#         return redirect('/pets')

# @csrf_exempt
# def purchase(request, pet_id):
#     if (request.method == 'POST'):
#         # this function creates and saves new customer
#         # and updates pet as sold
#         pet = get_object_or_404(Pet, pk=pet_id)
#         pet.sold = True
#         pet.save()

#         Cname = request.POST['name']
#         Cemail = request.POST['email']
#         Cphone = request.POST['phone']
#         Ccard = int(request.POST['card'])

#         new_customer = Customer(name=Cname, email=Cemail,
#                                 phone=Cphone, card=Ccard)
#         new_customer.save()

#         print(request.path)
#         # cant figure out how to redirect so that the adopted and button show up immediately
#         return render(request, 'pets/detail.html', {'info': pet})


# @csrf_exempt
# def delete(request, pet_id):
#     if (request.method == 'DELETE'):
#         pet = get_object_or_404(Pet, pk=pet_id)
#         # pet.delete()
#         # return redirect('/pets')
#         response = redirect('/pets')
#         # above works and gets a 200 at "http://localhost:8000/pets but page doesnt change
#         # method is delete on the redirect call not get for some reason
#         # return HttpResponseRedirect("http://localhost:8000/pets")
#         return response

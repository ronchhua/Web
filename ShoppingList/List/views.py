from django.shortcuts import render

# Create your views here.



from .models import List
from django.contrib import messages
from django.shortcuts import redirect


from .forms import ListForm

def index(request):
    
    sort = "neutral"
    Items = List.objects.all()
    return render(request, 'html/index.html', {'Items':Items, 'sort':sort})  #Unlike py4web you have to return (any vars) in curly braces. And render takes 3 arguments


#This is used to redirect to the form to fill in the product and also save the data

def add(request):  #So what I did is that when the client clicks on "Add" in the index.html it calls this view, which then REDIRECTS us to the html for adding something BECAUSE the response isn't a POST request. Then the button to add the product in this add_product.html will use this same function, but as a POST request and this will save the data entered there in a form

    if (request.method == 'POST'):  #Means we need to update table 

        if(request.POST.get('item') and request.POST.get('quantity') and request.POST.get('cost')):

            a = True

            try:
                int(request.POST.get('quantity'))
                float(request.POST.get('quantity'))
                int(request.POST.get('cost'))
                float(request.POST.get('cost'))

            except:
                
                a = False

            if(a):
                new_item = List()  #The name of the Table from models.py
                new_item.item = str(request.POST.get('item'))   #Allows integers to be a product name
                new_item.quantity = request.POST.get('quantity')
                new_item.cost = request.POST.get('cost')
                new_item.save()
                return redirect('index')  #The name of the URL for the main page

            else:
                
                messages.success(request, ('The Cost and Quantity must be Real Values!'))

                operation = "add"
                return render(request, 'html/add_product.html', {"operation" : operation})

            


    else:
        operation = "add"
        return render(request, 'html/add_product.html', {"operation" : operation})


def edit(request, product_id):

    if request.method == 'POST':
        item = List.objects.get(id=product_id)
        form = ListForm(request.POST or None, instance=item)
 
        if(request.POST.get('item') and request.POST.get('quantity') and request.POST.get('cost')):

            a = True

            try:
                int(request.POST.get('quantity'))
                float(request.POST.get('quantity'))
                int(request.POST.get('cost'))
                float(request.POST.get('cost'))

            except:
                
                a = False

            if(a and form.is_valid()):
                form.save()
                return redirect('index')

            else:
                
                messages.success(request, ('The Cost and Quantity must be Real Values!'))

                operation = "edit"
                return render(request, 'html/add_product.html', {'item' : item, "operation" : operation})


    else:
        item = List.objects.get(id=product_id)
        operation = "edit"

        return render(request, 'html/add_product.html', {'item': item, "operation" : operation})


def delete(request, product_id):
    
    item_to_delete = List.objects.get(id=product_id)
    item_to_delete.delete()

    return redirect('index')

def sorting(request, sort_value):

    #Reserved.objects.filter(client=id).order_by('-check_in')
    
    if (sort_value == "ascend"):

        List.objects.all().order_by('cost')
        Items = List.objects.all()
        sort = "ascending"
        return render(request, 'html/index.html', {'Items':Items, 'sort':sort})

    else:

        List.objects.all().order_by('-cost')
        Items = List.objects.all()
        sort = "descending"
        return render(request, 'html/index.html', {'Items':Items, 'sort':sort})

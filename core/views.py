from django.shortcuts import render 

 
# ----------------------------------------------------------------------
# Swagger UI + Admin + Doc API home page
# ----------------------------------------------------------------------
def home_index_page(request):
    return render(request, 'index.html')
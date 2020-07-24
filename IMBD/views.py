from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLInks
from django.shortcuts import get_object_or_404
# Create your views here.


class HomeView(ListView):
    model = Movie
    template_name = 'IMBD/index.html'
     
    #gives data to the template
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context

class MovieListView(ListView):
    model = Movie
    # template_name = "TEMPLATE_NAME"
    paginate_by = 2


class MovieDetailView(DetailView):
    model = Movie
    # template_name = "TEMPLATE_NAME"

    #This method will bring to us just a single movie
    def get_object(self):
        object = super(MovieDetailView, self).get_object()
        object.views_count +=1
        object.save()
        return object
    
    #we want to receive the links of the selected movie
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context["links"] = MovieLInks.objects.filter(movie = self.get_object()) 
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        print(context)
        return context
    

class MovieCategory(ListView):
    model = Movie
    template_name = "TEMPLATE_NAME"
    paginate_by = 2

    def get_queryset(self):
        self.category = self.kwargs['category'] 
        return Movie.objects.filter(category=self.category)

    #gives data to the template
    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category '] = self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    template_name = "TEMPLATE_NAME"
    paginate_by = 2

    def get_queryset(self):
        self.language = self.kwargs['lang']  
        return Movie.objects.filter(language=self.language)

    #gives data to the template
    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context

class MovieSearch(ListView):
    model = Movie
    template_name = "TEMPLATE_NAME"
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list =self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list 
        
class movieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True


class MostView(DetailView):
    model = Movie
    template_name = 'IMBD/most.html'
    
  
    # #gives data to the template
    def get_context_data(self, **kwargs):
        context = super(MostView, self).get_context_data(**kwargs)
        context['most_watched'] = Movie.objects.all(status='MW')
        return context


    

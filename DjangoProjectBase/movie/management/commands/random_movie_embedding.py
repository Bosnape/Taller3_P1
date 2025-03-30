import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Random embedding of a movie"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        movie = random.choice(movies)

        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
        print("Movie:", movie.title)
        print("Embedding:", embedding_vector)
        

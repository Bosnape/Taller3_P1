import os
import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images in the database from a folder"

    def handle(self, *args, **kwargs):
        # 📁 Ruta de la carpeta que contiene las imágenes
        image_folder = 'media/movie/images' # ← Cambia esto si es necesario
        
        # ✅ Verifica si la carpeta existe
        if not os.path.exists(image_folder):
            self.stderr.write(f"Folder not found.")
            return
        
        updated_count = 0
        
        for movie in Movie.objects.all():
            image_path = f"{image_folder}/m_{movie.title}.png" # Cambia la extensión si es necesario
            if os.path.exists(image_folder):
                movie.image = f"movie/images/m_{movie.title}.png"
                movie.save()
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(f"Updated: {movie.title}"))
        
        # ✅ Al finalizar, muestra cuántas películas se actualizaron
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movies from media folder."))
            
        
            
        

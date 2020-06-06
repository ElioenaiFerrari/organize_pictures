from PIL import Image
from datetime import datetime
import os
import shutil


class OrganizerModel:
    extensions = [
        'jpg',
        'jpeg',
        'png',
        'JPG',
        'JPEG',
        'PNG'
    ]

    def move_photo(self, file):
        new_folder = self.get_photo_path(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, f'{new_folder}/{file}')

    def get_photo_date(self, file):
        photo = Image.open(file)
        info = photo.getexif()
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def get_photo_path(self, file):
        date = self.get_photo_date(file)
        return f"{date.strftime('%Y')}/{date.strftime('%Y-%m-%d')}"

    def organize(self):
        photo = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext)) for ext in self.extensions
        ]

        for filename in photo:
            self.move_photo(filename)

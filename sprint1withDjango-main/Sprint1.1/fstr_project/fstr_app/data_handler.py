from .models import User, Coords, Pereval, PerevalImage

class DataHandler:

    @staticmethod
    def submit_data(data):
        user_data = data['user']
        coords_data = data['coords']
        images_data = data['images']

        # Создание или получение пользователя
        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults={
                'phone': user_data['phone'],
                'full_name': f"{user_data['fam']} {user_data['name']} {user_data['otc']}"
            }
        )

        # Создание координат
        coords = Coords.objects.create(
            latitude=coords_data['latitude'],
            longitude=coords_data['longitude'],
            height=coords_data['height']
        )

        # Создание перевала
        pereval = Pereval.objects.create(
            user=user,
            beauty_title=data['beauty_title'],
            title=data['title'],
            other_titles=data.get('other_titles', ''),
            connect=data.get('connect', ''),
            add_time=data['add_time'],
            coords=coords,
            level_winter=data['level'].get('winter', ''),
            level_summer=data['level'].get('summer', ''),
            level_autumn=data['level'].get('autumn', ''),
            level_spring=data['level'].get('spring', '')
        )

        # Добавление изображений
        for image in images_data:
            PerevalImage.objects.create(pereval=pereval, img=image['data'], title=image['title'])

        return pereval.id


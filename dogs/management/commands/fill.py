from django.core.management import BaseCommand
from dogs.models import Dogs, Breed


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_create(*args, **options)
        print("Success!!!")

    def clear_databases(self):
        Dogs.objects.all().delete()
        Breed.objects.all().delete()

    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """
        breed_list = [
            {"name": "Немецкий боксёр",
             "description": "Неме́цкий боксёр или просто боксёр (нем. Deutscher Boxer) — выведенная в Германии порода короткошёрстных служебных собак среднего размера. Предками боксёров были брабантский боевой пёс и английский бульдог. Порода относится к группе догообразных, или молоссов, — мощных широкотелых собак с крепким костяком и крупными головами. Боксёры — брахицефалы, обладают мощными челюстями и способны к захвату крупной добычи. Одна из самых популярных в мире пород собак."},
            {"name": "Английский бульдог",
             "description": "Англи́йский бульдо́г  (также бульдог, англ. bulldog, дословно: «бычья собака») — короткошёрстная порода собак типа мастифов. По способу использования стандарт относит породу к собакам-телохранителям и компаньонам[1]. Современные английские бульдоги выведены во второй половине XIX века, в основе породы — староанглийский бульдог, травильная порода собак, ныне вымершая. Английский бульдог обладает ярко выраженной индивидуальностью и считается национальной собакой Англии, воплощая черты, часто приписываемые «истинному джентльмену»[2]: основательность, невозмутимость, консервативность, некоторую флегматичность, с одной стороны, и аристократизм, солидность в сочетании с импозантностью и грубоватой элегантностью, с другой. Содержание бульдогов требует большой ответственности, так как порода в процессе развития, превратившись из бойцовой в декоративную, потеряла свои рабочие качества и стала весьма уязвимой. Этот факт часто отмечается критиками породы, предпринимаются попытки воссоздания оригинального староанглийского бульдога, однако признания со стороны Международной кинологической федерации эти опыты пока не получили."},
            {"name": "Пудель",
             "description": "Пу́дель (нем. Pudel, от puddeln — «плескаться в воде») — порода собак. Изначально пудель являлся рабочей собакой, в частности использовался на охоте. Современные пудели — преимущественно декоративные собаки. Пудель занимает второе место в рейтинге самых умных пород, составленном доктором Стенли Кореном, после бордер-колли. Они умеют приспосабливаться практически к любому климату."},
            {"name": "Колли",
             "description": "Ко́лли (англ. Collie) — группа пород пастушьих собак, происходящих из Шотландии и Северной Англии. Группа включает как официально признанные кинологическими организациями породы, так и малочисленные местные породы и отродья.\r\n\r\nКолли — пропорциональная собака среднего роста, достаточно лёгкого сложения, с заострённой мордой. Как правило, имеет характерную породную окраску. Колли активны, проворны и в большинстве случаев обладают ярко выраженным пастушьим инстинктом. Некоторые колли продолжают использоваться при выпасе крупного рогатого скота и овец. Другие содержатся в качестве компаньонов. Колли часто используются в кинологическом спорте, где они проявляют выдающиеся ловкость, выносливость и обучаемость.\r\n\r\nКолли широко распространены во всём мире, особенно популярны в Австралии и Северной Америке, где использовались для выведения других пастушьих пород, в том числе путём метизации с местными породами собак. Название породы может включать слово «колли», как, например, бордер-колли, но некоторые породы этого группового обозначения в своём названии не имеют. Первое упоминание о породе относится к 1790 году (Томас Вервик «История четвероногих»)."},
        ]
        breed_for_create = []
        for breed_item in breed_list:
            breed_for_create.append(Breed(**breed_item))
        Breed.objects.bulk_create(breed_for_create)

        dog_list = [
            {"name": "Мухтар", "breed": Breed.objects.get(name='Немецкий боксёр'), "photo": "dogs/photo/640px-Male_fawn_Boxer_undocked.jpg", "date_born": "2024-03-18"},
            {"name": "Джек", "breed": Breed.objects.get(name='Английский бульдог'), "photo": "dogs/photo/640px-Bulldog_inglese.jpg", "date_born": "2023-01-11"},
            {"name": "Принц", "breed": Breed.objects.get(name='Пудель'), "photo": "dogs/photo/599px-Poodle_Grand_2_Moletai_May_2014.jpg", "date_born": "2023-08-16"},
            {"name": "Пират", "breed": Breed.objects.get(name='Немецкий боксёр'), "photo": "dogs/photo/1000px-Male_Boxer.jpg", "date_born": "2022-09-30"},
            {"name": "Табби", "breed": Breed.objects.get(name='Пудель'), "photo": "dogs/photo/599px-Poodle_red.jpg", "date_born": "2022-11-21"},
            {"name": "Бетховен", "breed": Breed.objects.get(name='Английский бульдог'), "photo": "dogs/photo/anglijskij-buldog-960x540-1-960x540.jpg", "date_born": "2024-12-01"},
            {"name": "Акела", "breed": Breed.objects.get(name='Колли'), "photo": "dogs/photo/1000px-Male_Kolli.jpg", "date_born": "2022-01-11"}
        ]
        dog_for_create = []
        for dog_item in dog_list:
            dog_for_create.append(Dogs(**dog_item))
        Dogs.objects.bulk_create(dog_for_create)

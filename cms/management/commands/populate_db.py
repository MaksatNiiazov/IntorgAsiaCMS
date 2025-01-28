from django.core.management.base import BaseCommand
from cms.models1 import Contact, SocialMediaLink, Service, Advantage, BusinessTour

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными, если записи отсутствуют'

    def handle(self, *args, **kwargs):
        if not Contact.objects.exists():
            Contact.objects.create(
                name="Основной контакт",
                address="г. Бишкек, ул. Токтогула 123",
                phone="+996 700 123 456",
                email="info@example.com",
                whatsapp_link="https://wa.me/996700123456"
            )
            self.stdout.write(self.style.SUCCESS('Контакты добавлены.'))

        if not SocialMediaLink.objects.exists():
            SocialMediaLink.objects.create(platform="YouTube", url="https://youtube.com", icon=None)
            SocialMediaLink.objects.create(platform="Instagram", url="https://instagram.com", icon=None)
            self.stdout.write(self.style.SUCCESS('Ссылки на соцсети добавлены.'))

        if not Service.objects.exists():
            Service.objects.create(title="Фулфилмент", description="Полный цикл услуг по упаковке и отправке товаров", icon=None)
            Service.objects.create(title="Сертификация", description="Сертификация товаров для экспорта", icon=None)
            self.stdout.write(self.style.SUCCESS('Услуги добавлены.'))

        if not Advantage.objects.exists():
            Advantage.objects.create(title="Быстрая доставка", description="Доставка за 48 часов", icon=None)
            Advantage.objects.create(title="Лучшие цены", description="Конкурентоспособные цены на рынке", icon=None)
            self.stdout.write(self.style.SUCCESS('Преимущества добавлены.'))

        if not BusinessTour.objects.exists():
            BusinessTour.objects.create(
                name="Тур в Бишкек",
                description="Посещение фабрик, рынков и достопримечательностей",
                image=None,
                price="55000р"
            )
            BusinessTour.objects.create(
                name="Тур на Иссык-Куль",
                description="Программа с отдыхом у озера Иссык-Куль",
                image=None,
                price="65000р"
            )
            self.stdout.write(self.style.SUCCESS('Бизнес-туры добавлены.'))

        self.stdout.write(self.style.SUCCESS('Заполнение базы данных завершено.'))

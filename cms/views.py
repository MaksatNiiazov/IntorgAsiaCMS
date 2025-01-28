from django.shortcuts import render

from .models import BlockOrderingModel, MetaData, Contacts, HeaderSettingsModel, ServiceCategory


def home_view(request):
    """Отображение главной страницы с данными всех блоков."""
    meta_data = MetaData.objects.first()
    blocks = BlockOrderingModel.objects.order_by('order')
    contacts = Contacts.objects.first()
    header = HeaderSettingsModel.objects.first()

    context = {
        'meta_data': meta_data,
        'blocks': blocks,
        'contacts': contacts,
        'header': header,
    }

    return render(request, 'home.html', context)


def calculator_view(request):
    categories = ServiceCategory.objects.prefetch_related('services').all()
    contacts = Contacts.objects.first()
    context = {
        'categories': categories,
        'contacts': contacts
    }

    return render(request, 'calculator.html', context)
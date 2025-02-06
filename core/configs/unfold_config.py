from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Основная навигация"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Панель управления"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("Настройки сайта"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Шапка"),
                        "icon": "table_chart",
                        "link": reverse_lazy("admin:cms_headersettingsmodel_changelist"),
                    },
                    {
                        "title": _("Мета настройки"),
                        "icon": "psychology",
                        "link": reverse_lazy("admin:cms_metadata_changelist"),
                    },
                ],
            },

            {
                "title": _("Контентные блоки"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Блоки презентаций"),
                        "icon": "layers",
                        "link": reverse_lazy("admin:cms_presentationblockmodel_changelist"),
                    },
                    {
                        "title": _("Ключевые пункты"),
                        "icon": "list",
                        "link": reverse_lazy("admin:cms_keypointsblockmodel_changelist"),
                    },
                    {
                        "title": _("Изображения"),
                        "icon": "image",
                        "link": reverse_lazy("admin:cms_imageblockmodel_changelist"),
                    },
                    {
                        "title": _("Видео YouTube"),
                        "icon": "play_circle",
                        "link": reverse_lazy("admin:cms_youtubeblockmodel_changelist"),
                    },
                    {
                        "title": _("Слайды слайдера"),
                        "icon": "slideshow",
                        "link": reverse_lazy("admin:cms_sliderblockmodel_changelist"),
                    },
                    {
                        "title": _("Порядок блоков"),
                        "icon": "sort",
                        "link": reverse_lazy("admin:cms_blockorderingmodel_changelist"),
                    },
                ],
            },
            {
                "title": _("Контакты"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Контакты"),
                        "icon": "contacts",
                        "link": reverse_lazy("admin:cms_contacts_changelist"),
                    },
                ],
            },
            {
                "title": _("Услуги"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Категории услуг"),
                        "icon": "category",
                        "link": reverse_lazy("admin:cms_servicecategory_changelist"),
                    },
                    # {
                    #     "title": _("Услуги"),
                    #     "icon": "build",
                    #     "link": reverse_lazy("admin:cms_service_changelist"),
                    # },
                ],
            },
            {
                "title": _("Мета-настройки"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Мета-данные"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:cms_metadata_changelist"),
                    },
                ],
            },
        ],
    },
}

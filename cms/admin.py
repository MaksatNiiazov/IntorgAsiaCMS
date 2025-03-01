from django.contrib import admin
from django.contrib.auth.models import Group, User

from adminsortable2.admin import SortableAdminMixin
from unfold.admin import ModelAdmin, TabularInline

from .models import (
    MetaData,
    PresentationBlockModel,
    KeyPointsBlockModel,
    ImageBlockModel,
    YouTubeBlockModel,
    SliderBlockModel,
    SliderSlideModel,
    BlockOrderingModel,
    KeyPointModel,
    ButtonModel,
    HeaderSettingsModel,
    HeaderLinkModel,
    Contacts,
    SocialMediaLinkModel,
    EmailModel,
    PhoneModel,
    AddressModel,
    PopupModel,
    ServiceCategory,
    Service,
)


@admin.register(MetaData)
class MetaDataAdmin(ModelAdmin):
    pass


class HeaderLinkInline(TabularInline):
    model = HeaderLinkModel
    extra = 0


@admin.register(HeaderSettingsModel)
class HeaderSettingsAdmin(ModelAdmin):
    inlines = [HeaderLinkInline]


@admin.register(PresentationBlockModel)
class PresentationBlockAdmin(ModelAdmin):
    list_display = ('name', 'title', 'background_color')
    search_fields = ('name', 'title')


class KeyPointInline(TabularInline):
    model = KeyPointModel
    extra = 0


@admin.register(KeyPointsBlockModel)
class KeyPointsBlockAdmin(ModelAdmin):
    list_display = ('name', 'title',)
    search_fields = ('name', 'title')
    inlines = [KeyPointInline]


@admin.register(ImageBlockModel)
class ImageBlockAdmin(ModelAdmin):
    list_display = ('name', 'title', 'image')
    search_fields = ('name', 'title')


@admin.register(YouTubeBlockModel)
class YouTubeBlockAdmin(ModelAdmin):
    list_display = ('name', 'title', 'video_url')
    search_fields = ('name', 'title')


class SliderSlideInline(TabularInline):
    model = SliderSlideModel
    extra = 0


@admin.register(SliderBlockModel)
class SliderBlockAdmin(ModelAdmin):
    list_display = ('name', 'title', 'background_color')
    inlines = [SliderSlideInline]
    search_fields = ('name', 'title')


class ButtonInline(TabularInline):
    model = ButtonModel
    extra = 0


@admin.register(BlockOrderingModel)
class BlockOrderingAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('order', 'get_block_type', 'get_block_title')
    list_editable = ('order',)
    list_display_links = ('get_block_type',)
    search_fields = ('presentation_block__title', 'keypoints_block__title', 'image_block__title', 'slider_block__title')
    inlines = [ButtonInline]

    def get_block_type(self, obj):
        if obj.presentation_block:
            return "Презентация"
        elif obj.keypoints_block:
            return "Ключевые пункты"
        elif obj.image_block:
            return "Изображение"
        elif obj.slider_block:
            return "Слайдер"
        elif obj.youtube_block:
            return "Видео"
        elif obj.image_block:
            return "Изображение"
        return "Неизвестный"

    get_block_type.short_description = "Тип блока"

    def get_linked_block(self, obj):
        if obj.presentation_block:
            return obj.presentation_block
        elif obj.keypoints_block:
            return obj.keypoints_block
        elif obj.image_block:
            return obj.image_block
        elif obj.slider_block:
            return obj.slider_block
        elif obj.youtube_block:
            return obj.youtube_block
        elif obj.image_block:
            return obj.image_block
        return None

    get_linked_block.short_description = "Связанный блок"

    def get_block_title(self, obj):
        if obj.presentation_block:
            return obj.presentation_block.title
        elif obj.keypoints_block:
            return obj.keypoints_block.title
        elif obj.image_block:
            return obj.image_block.title
        elif obj.slider_block:
            return obj.slider_block.title
        elif obj.youtube_block:
            return obj.youtube_block.title
        elif obj.image_block:
            return obj.image_block.title
        return "Без заголовка"

    get_block_title.short_description = "Заголовок блока"


class SocialMediaLinkInline(TabularInline):
    model = SocialMediaLinkModel
    extra = 0


class EmailInline(TabularInline):
    model = EmailModel
    extra = 0


class PhoneInline(TabularInline):
    model = PhoneModel
    extra = 0


class AddressInline(TabularInline):
    model = AddressModel
    extra = 0


class PopupInline(TabularInline):
    model = PopupModel
    extra = 0


@admin.register(Contacts)
class ContactsAdmin(ModelAdmin):
    inlines = [SocialMediaLinkInline, EmailInline, PhoneInline, AddressInline, PopupInline]


class ServiceInline(TabularInline):
    model = Service
    extra = 0


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(SortableAdminMixin, ModelAdmin):
    inlines = [ServiceInline]




admin.site.unregister(Group)
admin.site.unregister(User)

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models

from cms.mixins import SingletonModelMixin


class MetaData(SingletonModelMixin, models.Model):
    meta_title = models.CharField(max_length=255, verbose_name="Мета заголовок", blank=True, null=True)
    meta_description = models.TextField(verbose_name="Мета описание", blank=True, null=True)
    meta_keywords = models.TextField(verbose_name="Мета ключевые слова", blank=True, null=True)
    meta_image = models.ImageField(upload_to='meta_images/', verbose_name="Мета изображение", blank=True, null=True)
    background_image = models.ImageField(upload_to='background_images/', verbose_name="Фоновое изображение", blank=True,
                                         null=True)
    favicon = models.ImageField(upload_to='favicon_images/', verbose_name="Favicon", blank=True, null=True)
    currency = models.CharField(max_length=10, verbose_name="Валюта в калькуляторе", blank=True, null=True)

    class Meta:
        verbose_name = "Мета-данные"
        verbose_name_plural = "Мета-данные"


class HeaderSettingsModel(SingletonModelMixin, models.Model):
    background_color = ColorField(verbose_name="Цвет фона", blank=True, null=True, format="hexa")

    class Meta:
        verbose_name = "Настройки шапки"
        verbose_name_plural = "Настройки шапки"


class HeaderLinkModel(models.Model):
    header = models.ForeignKey(HeaderSettingsModel, on_delete=models.CASCADE, verbose_name="Шапка",
                               related_name="links")
    text = models.CharField(max_length=255, verbose_name="Текст")
    text_color = ColorField(verbose_name="Цвет текста", blank=True, null=True, format="hex")
    link = models.CharField(max_length=255, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Ссылка в шапке"
        verbose_name_plural = "Ссылки в шапке"


class BaseBlockModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True, null=True)
    background_color = ColorField(verbose_name="Цвет фона", blank=True, null=True, format="hexa")
    background_image = models.ImageField(upload_to='blocks_backgrounds/', verbose_name="Фон", blank=True, null=True)
    text_color = ColorField(verbose_name="Цвет текста", blank=True, null=True, default="#000000")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PresentationBlockModel(BaseBlockModel):
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок", blank=True, null=True)
    text = models.TextField(verbose_name="Текст", blank=True, null=True)

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"


class KeyPointsBlockModel(BaseBlockModel):
    class Meta:
        verbose_name = "Ключевый пункт"
        verbose_name_plural = "Ключевые пункты"


class KeyPointModel(models.Model):
    block = models.ForeignKey(KeyPointsBlockModel, on_delete=models.CASCADE, verbose_name="Блок", related_name="points")
    icon = models.ImageField(upload_to='keypoints_icons/', verbose_name="Иконка", blank=True, null=True)
    invert_icon_color = models.BooleanField(default=False, verbose_name="Инвертировать цвет иконки")
    text = models.TextField(verbose_name="Текст", blank=True, null=True)

    def __str__(self):
        return self.text


class ImageBlockModel(BaseBlockModel):
    image = models.ImageField(upload_to='image_blocks/', verbose_name="Изображение", blank=True, null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class YouTubeBlockModel(BaseBlockModel):
    video_url = models.CharField(max_length=255, verbose_name="Ссылка на видео", blank=True, null=True)
    width = models.IntegerField(verbose_name="Ширина", blank=True, null=True)
    height = models.IntegerField(verbose_name="Высота", blank=True, null=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class SliderBlockModel(BaseBlockModel):
    pass

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class SliderSlideModel(models.Model):
    block = models.ForeignKey(SliderBlockModel, on_delete=models.CASCADE, verbose_name="Блок", related_name="slides")
    image = models.ImageField(upload_to='slider_slides/', verbose_name="Изображение", blank=True, null=True)


class BlockOrderingModel(models.Model):
    order = models.IntegerField(default=0, verbose_name="Порядок")
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)

    presentation_block = models.OneToOneField(
        'PresentationBlockModel',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Презентация"
    )
    keypoints_block = models.OneToOneField(
        'KeyPointsBlockModel',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Ключевые пункты"
    )
    image_block = models.OneToOneField(
        'ImageBlockModel',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Изображение"
    )

    youtube_block = models.OneToOneField(
        'YouTubeBlockModel',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Видео"
    )
    slider_block = models.OneToOneField(
        'SliderBlockModel',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name="Слайдер"
    )

    def get_block_type(self):
        if self.presentation_block:
            return "presentation"
        elif self.keypoints_block:
            return "keypoints"
        elif self.image_block:
            return "image"
        elif self.youtube_block:
            return "youtube"
        elif self.slider_block:
            return "slider"
        return "unknown"

    def clean(self):
        block_count = sum([
            bool(self.presentation_block),
            bool(self.keypoints_block),
            bool(self.image_block),
            bool(self.youtube_block),
            bool(self.slider_block)
        ])
        if block_count > 1:
            raise ValidationError("Блок может быть связан только с одним типом блока.")
        if block_count == 0:
            raise ValidationError("Блок должен быть связан хотя бы с одним типом блока.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']
        verbose_name = "Порядок блоков"
        verbose_name_plural = "Порядок блоков"

    def __str__(self):
        if self.presentation_block:
            return f"Презентация (Order: {self.presentation_block})"
        elif self.keypoints_block:
            return f"Ключевые пункты (Order: {self.keypoints_block})"
        elif self.image_block:
            return f"Изображение (Order: {self.image_block})"
        elif self.youtube_block:
            return f"Видео (Order: {self.youtube_block})"
        elif self.slider_block:
            return f"Слайдер (Order: {self.slider_block})"
        return f"Неизвестный блок (Order: {self.order})"


class ButtonModel(models.Model):
    block = models.ForeignKey(
        'BlockOrderingModel',
        on_delete=models.CASCADE,
        related_name='buttons',
        verbose_name="Блок"
    )
    text = models.CharField(max_length=255, verbose_name="Текст кнопки")
    url = models.CharField(max_length=255, verbose_name="Ссылка кнопки")
    background_color = ColorField(verbose_name="Цвет кнопки", blank=True, null=True, format="hexa")
    text_color = ColorField(verbose_name="Цвет текста", blank=True, null=True, default="#000000", format="hex")

    class Meta:
        verbose_name = "Кнопка"
        verbose_name_plural = "Кнопки"

    def __str__(self):
        return self.text


class Contacts(SingletonModelMixin, models.Model):
    background_color = ColorField(verbose_name="Цвет фона", blank=True, null=True, format="hexa")
    text_color = ColorField(verbose_name="Цвет текста", blank=True, null=True, default="#000000", format="hex")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class AddressModel(models.Model):
    contacts = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name="Контакты"
    )
    address = models.CharField(max_length=255, verbose_name="Название")
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"


class PhoneModel(models.Model):
    contacts = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
        related_name='phones',
        verbose_name="Контакты"
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    phone = models.CharField(max_length=255, verbose_name="Номер")
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


class EmailModel(models.Model):
    contacts = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
        related_name='emails',
        verbose_name="Контакты"
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)
    show_in_header = models.BooleanField(default=False, verbose_name="Показывать в шапке")

    class Meta:
        verbose_name = "Почта"
        verbose_name_plural = "Почты"


class SocialMediaLinkModel(models.Model):
    contacts = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
        related_name='social_media_links',
        verbose_name="Контакты"
    )
    platform = models.CharField(max_length=50, verbose_name="Платформа")
    url = models.CharField(max_length=255, verbose_name="Ссылка")
    icon = models.ImageField(upload_to='social_icons/', verbose_name="Иконка", blank=True, null=True)
    show_in_header = models.BooleanField(default=False, verbose_name="Показывать в шапке")

    def get_image_url(self):
        if self.icon:
            return self.icon.url
        return None

    class Meta:
        verbose_name = "Ссылка на соцсети"
        verbose_name_plural = "Социальные сети"


class PopupModel(models.Model):
    contacts = models.ForeignKey(
        'Contacts',
        on_delete=models.CASCADE,
        related_name='popups',
        verbose_name="Контакты"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True, null=True)
    phone_link = models.CharField(max_length=255, verbose_name="Ссылка на телефон", blank=True, null=True)
    whatsapp_link = models.CharField(max_length=255, verbose_name="Ссылка на WhatsApp", blank=True, null=True)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services",
                                 verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")
    main = models.BooleanField(default=False, verbose_name="Основная услуга")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    def __clean__(self):
        if self.main:
            Service.objects.filter(main=True).exclude(pk=self.pk).update(main=False)

    def save(self, *args, **kwargs):
        self.__clean__()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

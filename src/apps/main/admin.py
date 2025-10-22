from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Брендинг", {"fields": ("logo", "logo_preview", "slogan", "copyright_text", "tursab_image", "tursab_preview")}),  # noqa
        ("Контакты", {"fields": ("address", "email", "phone", "whatsapp")}),
    )
    readonly_fields = ("logo_preview", "tursab_preview")
    list_display = ("__str__", "email", "phone", "whatsapp")

    def has_add_permission(self, request):
        if models.SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.logo.url)  # noqa
        return "—"
    logo_preview.short_description = "Логотип (превью)"

    def tursab_preview(self, obj):
        if obj.tursab_image:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.tursab_image.url)  # noqa
        return "—"
    tursab_preview.short_description = "Турсаб (превью)"


class ExcursionImageInline(admin.TabularInline):
    model = models.ExcursionImage
    extra = 1
    fields = ("image", "caption", "sort_order", "thumb")
    readonly_fields = ("thumb",)

    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.image.url)  # noqa
        return "—"
    thumb.short_description = "Превью"


@admin.register(models.Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "updated_at", "cover_thumb")  # noqa
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "short_description", "content_md")
    inlines = (ExcursionImageInline,)
    readonly_fields = ("cover_thumb",)
    fieldsets = (
        (None, {"fields": ("title", "is_published")}),
        ("Контент", {"fields": ("short_description", "content_md")}),
        ("Изображения", {"fields": ("cover", "cover_thumb")}),
    )

    def cover_thumb(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.cover.url)  # noqa
        return "—"
    cover_thumb.short_description = "Превью"


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("full_name", "is_published", "created_at", "photo_thumb")
    list_filter = ("is_published", "created_at")
    search_fields = ("full_name", "text")
    readonly_fields = ("photo_thumb",)
    fields = ("full_name", "text", "is_published", "photo", "photo_thumb")

    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.photo.url)  # noqa
        return "—"
    photo_thumb.short_description = "Превью"


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "is_published", "sort_order")
    list_editable = ("is_published", "sort_order")
    search_fields = ("question", "answer")
    ordering = ("sort_order", "id")


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "fa_icon", "is_active", "sort_order")
    list_editable = ("is_active", "sort_order")
    search_fields = ("title", "url", "fa_icon")
    ordering = ("sort_order", "id")


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "is_active", "sort_order", "logo_thumb")
    list_editable = ("is_active", "sort_order")
    search_fields = ("name", "url")
    readonly_fields = ("logo_thumb",)
    fields = ("name", "url", "is_active", "sort_order", "logo", "logo_thumb")
    ordering = ("sort_order", "id")

    def logo_thumb(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.logo.url)  # noqa
        return "—"
    logo_thumb.short_description = "Превью"

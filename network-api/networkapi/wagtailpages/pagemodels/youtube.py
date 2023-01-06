from django.db import models
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail_localize.fields import SynchronizedField, TranslatableField

from ..utils import set_main_site_nav_information
from . import customblocks
from .customblocks.full_content_rich_text_options import full_content_rich_text_options
from .mixin.foundation_metadata import FoundationMetadataPageMixin


class YoutubeRegretsPage(FoundationMetadataPageMixin, Page):
    headline = models.CharField(
        max_length=500,
        help_text="Page headline",
        blank=True,
    )

    intro_text = StreamField(
        [
            ("text", blocks.CharBlock()),
        ], use_json_field=True
    )

    intro_images = StreamField(
        [
            ("image", customblocks.ImageBlock()),
        ], use_json_field=True
    )

    faq = StreamField(
        [("paragraph", blocks.RichTextBlock(features=full_content_rich_text_options))],
        blank=True,
        use_json_field=True
    )

    regret_stories = StreamField(
        [
            ("regret_story", customblocks.YoutubeRegretBlock()),
        ], use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        StreamFieldPanel("intro_text"),
        StreamFieldPanel("intro_images"),
        StreamFieldPanel("faq"),
        StreamFieldPanel("regret_stories"),
    ]

    translatable_fields = [
        # Promote tab fields
        SynchronizedField("slug"),
        TranslatableField("seo_title"),
        SynchronizedField("show_in_menus"),
        TranslatableField("search_description"),
        SynchronizedField("search_image"),
        # Content tab fields
        TranslatableField("title"),
        TranslatableField("headline"),
        TranslatableField("intro_text"),
        TranslatableField("intro_images"),
        TranslatableField("faq"),
        TranslatableField("regret_stories"),
    ]

    zen_nav = True

    def get_context(self, request):
        context = super().get_context(request)
        return set_main_site_nav_information(self, context, "Homepage")

    template = "wagtailpages/pages/youtube_regrets_page.html"


class YoutubeRegretsReporterPage(FoundationMetadataPageMixin, Page):
    headline = models.CharField(
        max_length=500,
        help_text="Page headline",
        blank=True,
    )

    intro_text = StreamField(
        [
            ("text", blocks.CharBlock()),
        ], use_json_field=True
    )

    intro_images = StreamField(
        [
            ("image", customblocks.ImageBlock()),
        ], use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        StreamFieldPanel("intro_text"),
        StreamFieldPanel("intro_images"),
    ]

    translatable_fields = [
        # Promote tab fields
        SynchronizedField("slug"),
        TranslatableField("seo_title"),
        SynchronizedField("show_in_menus"),
        TranslatableField("search_description"),
        SynchronizedField("search_image"),
        # Content tab fields
        TranslatableField("title"),
        TranslatableField("headline"),
        TranslatableField("intro_text"),
        TranslatableField("intro_images"),
    ]

    zen_nav = True

    def get_context(self, request):
        context = super().get_context(request)
        return set_main_site_nav_information(self, context, "Homepage")

    template = "wagtailpages/pages/youtube_regrets_reporter_page.html"


class YoutubeRegrets2021Page(FoundationMetadataPageMixin, Page):

    template = "wagtailpages/pages/youtube-regrets-2021/youtube_regrets_2021.html"
    max_count = 1
    zen_nav = True

    translatable_fields = [
        # Promote tab fields
        SynchronizedField("slug"),
        TranslatableField("seo_title"),
        SynchronizedField("show_in_menus"),
        TranslatableField("search_description"),
        SynchronizedField("search_image"),
        # Content tab fields
        TranslatableField("title"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        return set_main_site_nav_information(self, context, "Homepage")

    class Meta:
        verbose_name = "YouTube Regrets 2021 Page"
        verbose_name_plural = "YouTube Regrets 2021 Pages"


class YoutubeRegrets2022Page(FoundationMetadataPageMixin, Page):

    template = "wagtailpages/pages/youtube-regrets-2022/youtube_regrets_2022.html"
    max_count = 1
    zen_nav = True

    translatable_fields = [
        # Promote tab fields
        SynchronizedField("slug"),
        TranslatableField("seo_title"),
        SynchronizedField("show_in_menus"),
        TranslatableField("search_description"),
        SynchronizedField("search_image"),
        # Content tab fields
        TranslatableField("title"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        return set_main_site_nav_information(self, context, "Homepage")

    class Meta:
        verbose_name = "YouTube Regrets 2022 Page"
        verbose_name_plural = "YouTube Regrets 2022 Pages"


class YoutubeRegretsReporterExtensionPage(FoundationMetadataPageMixin, Page):

    template = "wagtailpages/pages/regrets-reporter-landing-page/youtube_regrets_reporter_extension.html"
    max_count = 1
    zen_nav = True

    translatable_fields = [
        # Promote tab fields
        SynchronizedField("slug"),
        TranslatableField("seo_title"),
        SynchronizedField("show_in_menus"),
        TranslatableField("search_description"),
        SynchronizedField("search_image"),
        # Content tab fields
        TranslatableField("title"),
    ]

    content_panels = Page.content_panels  # Needed for wagtail-modeltranslation to work

    def get_context(self, request):
        context = super().get_context(request)
        return set_main_site_nav_information(self, context, "Homepage")

# Generated by Django 3.2.20 on 2023-08-09 15:07

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailpages", "0098_pni_increase_char_limits_again"),
    ]

    operations = [
        migrations.AddField(
            model_name="rcclandingpage",
            name="aside_cta",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(help_text="Heading for the card.")),
                                ("body", wagtail.blocks.TextBlock(help_text="Body text of the card.")),
                                (
                                    "button",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("label", wagtail.blocks.CharBlock()),
                                            ("URL", wagtail.blocks.CharBlock()),
                                            (
                                                "styling",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("btn-primary", "Primary button"),
                                                        ("btn-secondary", "Secondary button"),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AddField(
            model_name="researchlandingpage",
            name="aside_cta",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(help_text="Heading for the card.")),
                                ("body", wagtail.blocks.TextBlock(help_text="Body text of the card.")),
                                (
                                    "button",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("label", wagtail.blocks.CharBlock()),
                                            ("URL", wagtail.blocks.CharBlock()),
                                            (
                                                "styling",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("btn-primary", "Primary button"),
                                                        ("btn-secondary", "Secondary button"),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]

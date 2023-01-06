# Generated by Django 3.2.13 on 2022-10-05 07:14

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailpages", "0043_adds_listing_block"),
    ]

    operations = [
        migrations.AddField(
            model_name="banneredcampaignpage",
            name="aside",
            field=wagtail.fields.StreamField(
                [
                    (
                        "linkbutton",
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
                    (
                        "spacer",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("1", "quarter spacing"),
                                            ("2", "half spacing"),
                                            ("3", "single spacing"),
                                            ("4", "one and a half spacing"),
                                            ("5", "triple spacing"),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-02 08:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('fgis_cms', '0002_auto_20200802_0711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fgiscmspage',
            options={'verbose_name': 'Theme Page', 'verbose_name_plural': 'Theme Pages'},
        ),
        migrations.RenameField(
            model_name='fgiscmspage',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='fgiscmspage',
            name='background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='fgiscmspage',
            name='resources',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]

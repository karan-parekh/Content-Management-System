# Generated by Django 3.1.7 on 2021-03-25 07:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210325_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='contents', to='core.user'),
            preserve_default=False,
        ),
    ]

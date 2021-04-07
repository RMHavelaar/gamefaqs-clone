# Generated by Django 3.0.8 on 2021-04-07 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('topic', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('platforms', models.CharField(choices=[('1', 'PC'), ('2', 'PS5'), ('3', 'XSX'), ('4', 'Switch'), ('5', 'iOS'), ('6', 'Android'), ('7', 'Arcade'), ('8', 'PS4'), ('9', 'PS3'), ('10', 'Xbox One'), ('11', 'Xbox 360'), ('12', 'Sega'), ('13', 'Wii U'), ('14', 'Wii'), ('15', 'PSP'), ('16', 'Vita'), ('17', '3DS'), ('18', 'RetroPy'), ('19', 'Other Systems')], max_length=50)),
                ('user_posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

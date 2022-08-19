# Generated by Django 4.0.6 on 2022-08-19 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_alter_card_issuer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipient',
            old_name='profilepicture',
            new_name='profile_picture',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account'),
        ),
    ]

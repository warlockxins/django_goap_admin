# Generated by Django 4.1.2 on 2023-04-29 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goap', '0003_actionstate_variable'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionstate',
            name='planDomain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goap.plandomain'),
            preserve_default=False,
        ),
    ]

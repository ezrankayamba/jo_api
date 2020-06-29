# Generated by Django 3.0.6 on 2020-05-23 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200523_1048'),
        ('sales', '0014_auto_20200523_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('commission_rate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tonage', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.IntegerField(default=0)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Agent')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='sales.Invoice'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-02 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fofo', '0002_alter_profile_doctor_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('اطفال حديثي الولاده', 'اطفال حديثي الولاده'), ('جراحه اورام', 'جراحه اورام'), ('عظام', 'عظام'), ('اسنان', 'اسنان'), ('جراحه اوعيه دمويه', 'جراحه اوعيه دمويه'), ('باطنه', 'باطنه'), ('قلب و اعيه دمويه', 'فلب و اعيه دمويه'), ('انف و اذن', 'انف و اذن'), ('نفسي', 'نفسي'), ('امراض دم', 'امراض دم'), ('اورام', 'اورام'), ('جلديه', 'جلديه'), ('تخسيس و تغذيه', 'تخسيس و تغذيه'), ('جراحه سمنه و مناظير', 'جراحه سمنه و مناظير'), ('مخ و اعصاب', 'مخ و اعصاب'), ('جراحه تجميل', 'جراحه تجميل'), ('نساء و توليد', 'نساء و توليد'), ('جراحه اطفال', 'جراحه اطفال')], max_length=50, null=True, verbose_name='الدكتور ؟'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('رجل', 'رجل'), ('انثي', 'انثي')], max_length=50, verbose_name='النوع:'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fofo.profile')),
            ],
        ),
    ]

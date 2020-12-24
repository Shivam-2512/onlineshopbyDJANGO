
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('haed0', models.CharField(default='', max_length=50)),
                ('head1', models.CharField(default='', max_length=50)),
                ('head2', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]

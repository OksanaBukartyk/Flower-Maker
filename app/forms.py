from django.forms import ModelForm, Textarea

from app.models import Product,Version


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        prefix='product_form'
        fields = '__all__'
        # fields = ['headline', 'thumbnail', 'category', 'description']
        labels = {'headline': ('Назва'), 'thumbnail': ('Основне фото'), 'description': ('Опис')}
        help_texts = {'headline': ('Коротко і ясно'), 'thumbnail': ('Буде показано в пошуку'),
                      'description': ('Детальна інформація про товар')}

        #exclude = ['author', 'slug', 'active', 'featured']
        # fields = ['headline', 'tags', 'author', 'product_category', ]



class ProductVersionCreateForm(ModelForm):
    class Meta:
        prefix = 'version_form'
        model=Version
        fields='__all__'
        exclude = ['product_id']
        labels={'color':('Color name?')}
        widgets = {
            'color': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

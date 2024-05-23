import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from accounts.manager import UserManager
from django.core.validators import FileExtensionValidator
                                    

class UserProfile(AbstractUser):
    mobile_number = PhoneNumberField(_("Mobile Number"),unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile_number'
    # REQUIRED_FIELDS = ['mobile_number']

    def __str__(self):
        return self.mobile_number.as_e164 
    

class ProductCategory(models.Model):
    category_name = models.CharField(_('Category Name'),max_length=200)
    image = models.ImageField(_('Image'),
        validators =[FileExtensionValidator(allowed_extensions=['JPEG','JPG','PNG'])],
        upload_to ='./category/image',null = True,blank = True,)
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Category"
    

class Brand(models.Model):
    brand_name = models.CharField(_('Brand Name'),max_length=225,)
    image = models.ImageField(_('Brand Logo'),
        validators=[FileExtensionValidator(allowed_extensions=[ 'JPEG', 'PNG', 'JPG'])],
        upload_to="./brand/image",null = True,blank = True)


# Product Model
TAX_RATE_CHOICES = (
    ('12','12%'),
    ('18','18%'),
    ('28','28%'),
)

class Product(models.Model):
    popular = models.BooleanField(default=False,blank=True)
    product_number = models.CharField(_('Product Number'),max_length=100,help_text='generated automatically',blank= True,null=True)
    product_name = models.CharField( _('Product Name'),max_length=500)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,verbose_name=_('Category'),related_name='product',)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name=_('Brand'),related_name='product',null=True,blank=True)
    price = models.FloatField(_('Price'),default=0,)
    tax_rate = models.CharField(_('Tax Rate'),max_length=5,choices=TAX_RATE_CHOICES,null=True,blank=True)
    is_active = models.BooleanField(_('Is Active'),default=True)
    description = models.TextField( _('Description'), max_length=10000,null=True,blank=True)
    image = models.ImageField(_('Main Image'),max_length=1000,validators=[FileExtensionValidator(allowed_extensions=['JPEG', 'PNG', 'JPG'])],
                              upload_to="./product/image",null = True,blank = True,)
    added_by = models.ForeignKey(UserProfile,verbose_name=_('Added By'),related_name="product",on_delete=models.CASCADE,null=True,blank=True,)
    created_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)

    def save(self, *args, **kwargs):
        product_name = self.product_name
        if not self.product_number:
            random_num = random.randint(0, 99)
            self.product_number = (
                product_name[:5:2]).upper()+str(random_num)
        else:
            self.product_number = self.product_number
        super(Product, self).save(*args, **kwargs)
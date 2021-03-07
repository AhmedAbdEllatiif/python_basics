from django.db import models
from django.contrib.auth.models import User 
import datetime
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
import datetime
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

    


class Product(models.Model):
    
    class ProductRate(models.IntegerChoices):
        EXCELLENT = 5 
        GREAT = 4
        GOOD = 3
        ACCEPTED = 2
        POOR = 1
        NOTRATED = 0
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=19,decimal_places=2)
    rate = models.IntegerField(choices=ProductRate.choices,default=ProductRate.NOTRATED)
    slug = models.SlugField(unique=True,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
  
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("main-app:product_by_id", kwargs={"slug": self.slug})
    
    def update_model(self):
        product = Product.objects.get(id=self.id)
        print(product)
        # Do some stuff, update your model...
        Product.objects.filter(id=product.id).update(slug=product.id)

    @property
    def images(self):
        products_image = ProductImage.objects.filter(product=self.id)
        print(">>>>>>>>>>>Count: " ,products_image.count())
        imgs = []
        for product_img in products_image:
            img = product_img.image.url
            imgs.append(img)
        return imgs        
    
    
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
            # Get the maximum display_id value from the database
           
            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
        super(Product, self).save(*args, **kwargs)
        self.update_model()
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploaded_images")

    def __str__(self):
        return self.product.title
    
    
    
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
   
  
    @property
    def total_price(self):
        current_product = self.product
        price = current_product.price
        return price * self.quantity
    
    @property
    def item_price(self):
        current_product = self.product
        price = current_product.price
        return price
    
    def __str__(self):
        return self.product.title
    
    

class Order(models.Model):
    
    class OrderStatus(models.IntegerChoices):
        CREATED = 0
        PENDING = 1
        SHIPPING = 2
        DELIVERD = 3
    
    
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    order_status = models.IntegerField(choices=OrderStatus.choices, default=OrderStatus.CREATED)
    user_commnet = models.TextField(null=True,blank=True)
    order_num = models.PositiveIntegerField(default=1000,validators=[MinValueValidator(1000)])
    created_at = models.DateTimeField(default=datetime.datetime.now())
    items = models.ManyToManyField(OrderItem)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True,blank=True)
    slug = models.SlugField(default=1000)
    
    
    def get_absolute_url(self):
        return reverse("main-app:order_by_id", kwargs={"slug": self.slug})
    
    
    @property
    def total_amount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_price
            
        return total


    @property
    def products(self):
        lst = []
        
        for item in self.items.all():
            imgs =  []
            for img in ProductImage.objects.filter(product=item.product):
                
                imgs.append(img.image.url)

                
            lst.append({
                "title" :item.product.title,
                "image": imgs,
                "desc" :item.product.description,
                "quantity" : item.quantity,
                "price" :item.product.price,
                "rate" :item.product.rate,
            })
            
           
        return lst
    
    @property 
    def products_count(self):
        return  self.items.count()
  
    
 
    def update_model(self):
            #print(">>>>>>>>>>>>>>>> Slug ")
            current_order = Order.objects.filter(id=self.id)
            num =  1000 + int(self.id)
            #print(">>>>>>>>>>>>>>>> Slug num " , num)
            slug_num= slugify(num)
            current_order.update(order_num= num,slug = slug_num) 
            
        

    def save(self, *args, **kwargs):
        """ if self._state.adding:
            last_order_num = Order.objects.all().aggregate(largest=models.Max('order_num'))['largest']
                # aggregate can return None! Check it first.
                # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_order_num is not None:
                self.order_num = last_order_num + 1
                self.slug = slugify(last_order_num + 1) """
        super(Order, self).save(*args, **kwargs)
        self.update_model()

    """ def save(self, *args, **kwargs):
        
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            print(">>>>>>>>>>>.self._state.adding")
            # Get the maximum display_id value from the database
            last_order_num = Order.objects.all().aggregate(largest=models.Max('order_num'))['largest']
            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_order_num is not None:
                self.order_num = last_order_num + 1
                print(">>>>>>>>>>>.last_order_num",last_order_num)
                self.slug = slugify(last_order_num + 1)
                
        super(Order, self).save(*args, **kwargs) """
   
        
   
        
    
    
    
    
    
    

from django.db import models

# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(BaseModel):
    name = models.CharField(max_length = 20)
    mobile_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    otp = models.CharField(null=True, blank=True)
    otp_used = models.CharField(null=True, blank=True)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return f"{self.name}-{self.id}"
        
class Generated_image(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    system_prompt = models.TextField()
    user_prompt = models.TextField()
    image = models.FileField(upload_to="backoffice_engine/user_generated_image", null=True, blank=True)
    temprature = models.FloatField()
    class Meta:
        db_table = 'generated_image'
    
    def __str__(self):
        return f"{self.id} - {self.user} - {self.system_prompt} - {self.user_prompt} - {self.image} - {self.temprature} "
######################################################## TO DO DELETE WHEN USER DELETED

class Plan(BaseModel):
    name = models.CharField(max_length = 50)
    description = models.TextField(null= True,blank=True)
    price = models.IntegerField(null=False,blank=False)
    duration_days = models.IntegerField()
    credit=models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default = True)  

    class Meta:
        db_table = 'plan'
    
    def __str__(self):
        return f"{self.name} -- {self.credit}" 

class Category(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    
    class Meta: 
        db_table = 'category'
    
    def __str__(self):
        return f"{self.id} -- {self.name} -- {self.description}"

class Suggested_prompt(BaseModel):
    prompt = models.TextField(null=True)

    class Meta:
        db_table = 'sugested_prompt'
    
    def __str__(self):
        return f"{self.prompt}"

class Subscription(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='active')
    pending_credit=models.IntegerField(default=0)

    class Meta:
        db_table = 'subscription'
    
    def __str__(self):
        return f"{self.id} -- {self.user.name} -- {self.start_date} -- {self.end_date} -- {self.status} -- {self.pending_credit}"


class Feedback(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'feedback'
    
    def __str__(self):
        return f"{self.user.id} -- {self.user.name} -- {self.comment}"
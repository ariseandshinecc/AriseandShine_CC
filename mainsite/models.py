#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from django.db import models
from django.urls import reverse
import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class Address(models.Model):
    """
    Cbo's address.
    """
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, 
        help_text='You need to state explicitly the current profile of the cbo for this address')
    physical_address = models.CharField(max_length=100)
    postal_address = models.PositiveSmallIntegerField()
    postal_code = models.PositiveIntegerField()
    city = models.CharField('City/Town', max_length=50) 
    site_map = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return f'{self.physical_address}, P.O BOX {self.postal_address} - {self.postal_code}, {self.city}'
    

class Career(models.Model):
    """
    Record of job opportunities including voluntary
    put up by the cbo singly or through partnership
    """
    career_choices = [
        ('v', 'voluntary'),
        ('i', 'internship'),
        ('p', 'Permanent'),
        ('c', 'Contract'),
        ('u', 'uncategorized')
    ]
    position = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=career_choices, default='u')
    date_posted = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField('job start date', blank=True, null=True)
    end_date = models.DateField('job end date', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.position
    

    def get_absolute_url(self):
        return reverse("career-detail", kwargs={"slug": self.slug})

class Contact(models.Model):
    """
    Record of the cbo's contacts e.g 
    social media links, phone, address
    """
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, 
        help_text="State the cbo's profile for these contacts")
    phone = PhoneNumberField(
        help_text="Enter phone number in the international format<br>e.g +2547xxxxxxxx"
    )
    whatsapp = PhoneNumberField(
        help_text="Enter the whatsapp number in the international format<br>e.g +2547xxxxxxxx"
    )
    facebook = models.URLField()
    twitter = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.profile} contact'
    


class Donation(models.Model):
    """
    Record of donations received in kind
    """
    donor_choices = [
        ('ind', 'Individual'),
        ('org', 'Organization'),
        ('gov', 'Government'),
        ('unc', 'Uncategorized')
    ]
    donor_name = models.CharField(max_length=50, unique=True)
    donor_category = models.CharField(
        max_length=3, choices=donor_choices, default='unc', blank=True)
    pledge = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField("Reference link", blank=True, null=True)
    logo = models.ImageField(upload_to='images/logos', null=True, blank=True)

    def __str__(self):
        return self.donor_name
    

class Impact(models.Model):
    """
    Record of impacts for stated project.
    """
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    impact_text = models.TextField('impact')

    def __str__(self):
        return self.impact_text
    

class Job_Requirement(models.Model):
    """
    Record of job requirements for an advertised job.
    """
    job = models.ForeignKey(Career, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Job requirement" # Remove underscore for this model display in admin panel

    def __str__(self):
        return self.requirement
    

class Job_Description(models.Model):
    """
    Record of the job responsibities for an advertised job.
    """
    job = models.ForeignKey(Career, on_delete=models.CASCADE)
    responsibility = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Job description" # Remove underscore for this model display in admin panel

    def __str__(self):
        return self.responsibility

class Media(models.Model):
    """
    Record of the cbo's media, 
    currently only photos are supported
    """
    picture = models.ImageField(upload_to='images/%Y/%m/%d/', 
        help_text="Filesize should not be more than 5mb, Compress first if otherwise")
    caption = models.CharField('picture caption', max_length=256, 
        help_text="Provide a caption text of not more than 256 characters", unique=True)
    carousel = models.BooleanField("display on the carousel", default=False, 
        help_text="Select this check to show this picture on the homepage slideshow")

    class Meta:
        verbose_name_plural = 'Media'

    def __str__(self):
        return self.caption
    

class Member(models.Model):
    """
    Record of the cbo members' details.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(unique=True, max_length=15)
    date_of_birth = models.DateField(blank=True, default='1970-07-01')
    phone_number = PhoneNumberField(
        help_text="Enter phone number in the international format<br>e.g +2547xxxxxxxx"
    )
    email_address = models.EmailField(blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=50, default='member', blank=True)
    profile_photo = models.ImageField(
        upload_to='images/profiles/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Message(models.Model):
    """
    Record of reachouts and enquiries to the cbo.
    """
    sender_name = models.CharField('name', max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField()
    time_of_receipt = models.DateTimeField('received on', auto_now_add=True)

    def __str__(self):
        return self.sender_name

    def save(self, *args, **kwargs):
        print("Sending message...")
        super().save(*args, **kwargs)
        print("Message Sent")

class NewsEvent(models.Model):
    """
    Record of news and events of the cbo 
    or related to the cbo
    """
    headline = models.CharField(max_length=200, unique=True)
    media = models.ManyToManyField(Media, blank=True, 
        help_text="Choose a picture for this news or event")
    content = models.TextField()
    external_link = models.URLField(null=True, blank=True)
    pub_date = models.DateTimeField('publication date', 
        help_text="If you enter a future date, the event will be posted on that date you have entered")
    slug = models.SlugField(max_length=200, unique=True, null=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'News and Event'
        verbose_name_plural = 'News and Events'

    def __str__(self):
        return self.headline

    # Lets you view news or event instance on the public site
    #def get_absolute_url(self):
    #    return reverse("event_detail", kwargs={"slug": self.slug})
    
    

class Objective(models.Model):
    """
    Record of the cbo's objectives
    """
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, 
    help_text="State the cbo's profile for this objective")
    objective = models.TextField()

    def __str__(self):
        return self.objective

class Partner(models.Model):
    """
    Record of donations to the cbo
    """
    partner_choices = [
        ('Gov', 'Government Entity'),
        ('NGO', 'Non-Governmental Organization'),
        ('CBO', 'Community Based Organization'),
        ('SHP', 'Self-Help Group'),
        ('UNC', 'Uncategorized')
    ]
    partner_name = models.CharField(max_length=50, unique=True)
    partner_category = models.CharField(
        max_length=3, choices=partner_choices, default='UNC', blank=True)
    link = models.URLField('reference link', blank=True, null=True)
    logo = models.ImageField(upload_to='images/logos', null=True, blank=True)

    def __str__(self):
        return self.partner_name

class Profile(models.Model):
    """
    Record of the important editable CBO's information
    such as name, story, mission, vision, slogan
    """
    brand = models.CharField(max_length=50, default='Arise and shine Care Centre', editable=True) 
    about = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    slogan = models.CharField(max_length=200)

    def __str__(self):
        return self.brand
    
    class Meta:
        db_table = 'profile'
        verbose_name = "Arise and Shine Profile"
        verbose_name_plural = 'Arise and Shine Profile'

    
    
class Project(models.Model):
    """
    Record of cbo's projects and programmes
    """
    themes = [
        ('livelihood', 'Livelihood'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('environment', 'Environment'),
        ('social-Protection', 'Social Protection')
    ]

    project_name = models.CharField(max_length=200, unique=True)
    thematic_area = models.CharField(max_length=17, choices=themes)
    project_description = models.TextField()

    partners = models.ManyToManyField('Partner', blank=True,
                                      help_text='Select partners for this project if any')
    donations = models.ManyToManyField('Donation', blank=True,
                                       help_text='Select donors for this project if any')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, verbose_name="Ended")
    media = models.ManyToManyField(Media, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    class Meta:
        ordering = ['-start_date', 'end_date']

    def __str__(self):
        return self.project_name

    # Lets you view a project instance on the public site
    def get_absolute_url(self):
        return reverse("mainsite:project_details", kwargs={'thematic_area': self.thematic_area, 'slug':self.slug})

    def show_partners(self):
        """Return comma-separated project instance partners."""
        return ', '.join(partner.partner_name for partner in self.partners.all())

    def show_donors(self):
        """Return comma-separated project instance donations."""
        return ', '.join(donation.donor_name for donation in self.donations.all())

    def has_ended(self):
        if self.end_date == None or self.end_date > datetime.date.today():
            return "Ongoing"

        return self.end_date

    show_partners.short_description = "Partners"
    show_donors.short_description = "Financiers"
    has_ended.short_description = "Completion date"



class Value(models.Model):
    """
    CBO's core values
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    core_value = models.CharField(max_length=200)

    def __str__(self):
        return self.core_value
    
    class Meta:
        verbose_name = "Core value"
        verbose_name_plural = "Core values"

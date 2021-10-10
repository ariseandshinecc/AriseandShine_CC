#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from django.contrib import admin
from mainsite import models as app_models
# Register your models here.


class ObjectiveInline(admin.TabularInline):
    model = app_models.Objective
    fields = ['objective']
    extra = 0

class ValueInline(admin.TabularInline):
    model = app_models.Value
    fields = ['core_value']
    extra = 0

@admin.register(app_models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Profile', {'fields':['brand', 'about', 'slogan']}),
        ('Mission', {'fields': ['mission']}),
        ('Vision', {'fields': ['vision']}),
    ]

    inlines = [ObjectiveInline, ValueInline]

    list_display = ['brand', 'slogan', 'mission', 'vision']

@admin.register(app_models.Member)
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Bio data', {'fields': ['first_name', 'last_name', 'other_names', 'id_number', 'date_of_birth']}),
        ('Contact information', {'fields': ['phone_number', 'email_address']}),
        ('Other information', {'fields': ['designation', 'profession', 'occupation']}),
        ('Profile photo', {'fields': ['profile_photo']})
    ]

    list_display = ['first_name', 'last_name', 'id_number', 'date_of_birth', 'phone_number', 'email_address', 'designation']
    list_filter = ['designation']
    list_editable = ['date_of_birth']
    list_per_page = 10



class ImpactInline(admin.TabularInline):
    model = app_models.Impact
    fields = ['impact_text']
    extra = 0

@admin.register(app_models.Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project info', {'fields': ['thematic_area', 'project_name', 'project_description']}),
        ('Support', {'fields': ['partners', 'donations']}),
        ('Project Timeline', {'fields': ['start_date', 'end_date']}),
        ('Project Media', {'fields': ['media']}),
        ('Other', {'fields': ['slug']}),
    ]
    inlines = [ImpactInline]
    list_display = ['project_name', 'start_date', 'has_ended', 'show_donors', 'show_partners']
    list_filter = ['thematic_area', 'start_date']
    search_fields = ['project_name']
    list_per_page = 10
    date_hierarchy = 'start_date'
    prepopulated_fields = {'slug': ('project_name',)}

@admin.register(app_models.Message)
class MessageAdmin(admin.ModelAdmin):
    fields = (('sender_name', 'phone_number', 'email'), 'message')
    list_display = ['sender_name', 'phone_number', 'email', 'time_of_receipt']
    readonly_fields = ['sender_name', 'phone_number', 'email', 'message']
    date_hierarchy = 'time_of_receipt'


class DescriptionInline(admin.TabularInline):
    model = app_models.Job_Description
    fields = ['responsibility']
    extra = 0

class RequirementInline(admin.TabularInline):
    model = app_models.Job_Requirement
    fields = ['requirement']
    extra = 0

@admin.register(app_models.Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['position', 'date_posted']
    inlines = [DescriptionInline, RequirementInline]
    date_hierarchy = 'date_posted'
    prepopulated_fields = {'slug': ('position', )}



@admin.register(app_models.NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ['headline', 'pub_date', 'external_link']
    list_filter = ['pub_date']
    list_per_page = 10
    date_hierarchy = 'pub_date'
    filter_vertical = ['media']
    prepopulated_fields = {'slug': ('headline', )}


@admin.register(app_models.Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'donor_category']
    list_filter = ['donor_category']


@admin.register(app_models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['partner_name', 'partner_category']
    list_filter = ['partner_category']


@admin.register(app_models.Media)
class MediaAdmin(admin.ModelAdmin):
    #fields = (('caption', 'picture'), 'carousel')
    fieldsets = [
        (None, {'fields': ['picture', 'caption', 'carousel'],
         'description': '<h1 style="color: brown">Take great care not to upload too many or unnecessary photos</h1>'})
    ]
    list_display = ('caption', 'picture', 'carousel')
    list_per_page = 10

@admin.register(app_models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'whatsapp', 'email', 'facebook', 'twitter')

@admin.register(app_models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('physical_address', 'postal_address', 'postal_code', 'city')

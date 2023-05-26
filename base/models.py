from django.db import models
from django.utils import timezone
# Create your models here.


class logo(models.Model):
    L_id = models.IntegerField(primary_key=True)
    Reson = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='logo',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)
    class Meta:
          get_latest_by = ['image']

class Gallery(models.Model):
    G_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Gallery/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now)

class Events(models.Model):
    E_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Events/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now)
    last_updated_date = models.DateField(default=timezone.now)

class Awards(models.Model):
    E_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Awards/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    Awardee = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now)
    last_updated_date = models.DateField(default=timezone.now)

class Testimonials(models.Model):
    T_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Testimonials/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class Team(models.Model):
    Team_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Team/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    linkedin = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class Partners(models.Model):
    P_id = models.IntegerField(primary_key=True)
    categories = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Partners/%Y/%m/%d',default='images/user_image.png')
    Name = models.CharField(max_length = 200)

class Vision(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)
    description = models.CharField(max_length = 200)

class Mission(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)
    description = models.CharField(max_length = 200)

class Value(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)
    description = models.CharField(max_length = 200)

class About(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)
    description = models.CharField(max_length = 200)

class Latest_News(models.Model):
    L_id = models.IntegerField(primary_key=True)
    News = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class About_SISFS(models.Model):
    FD_id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class Facilities_developed(models.Model):
    FD_id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)


class Carrer(models.Model):
    id              = models.IntegerField(primary_key=True)
    updated_date    = models.DateField(default=timezone.now)
    Name   = models.CharField(max_length = 200)
    image           = models.ImageField(upload_to='Carrer/%Y/%m/%d',default='carrer/Screenshot_3.png')
    Email            = models.CharField(max_length = 200)
    Message     = models.CharField(max_length = 200,default='designation')
    Subject      = models.CharField(max_length = 200,default='department')
    qualififcation  = models.CharField(max_length = 200,default='qualififcation')
    experience      = models.IntegerField(default=0)

class blog(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    description     = models.CharField(max_length = 200,default = "Author not provied any description")
    content         = models.CharField(max_length = 2000,default = "Author not provied any description")
    blog_profile_img = models.CharField(max_length = 2000,default = "https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X")
    categories = models.CharField(max_length = 200)
    updated_date    = models.DateField(default=timezone.now)

class Birac(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    image           = models.ImageField(upload_to='Birac/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
class Tbi(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    updated_date    = models.DateField(default=timezone.now)
    
class Sisfs(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    image           = models.ImageField(upload_to='Sisfs/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
class EventsForm(models.Model):
    id              = models.IntegerField(primary_key=True)
    updated_date    = models.DateField(default=timezone.now)
    title = models.CharField(max_length = 200,default='title')
    Name   = models.CharField(max_length = 200)
    image           = models.ImageField(upload_to='EventsForm/%Y/%m/%d',default='carrer/Screenshot_3.png')
    Email            = models.CharField(max_length = 200)
    company     = models.CharField(max_length = 200,default='company')
    event      = models.CharField(max_length = 200,default='event')
    linkedin  = models.CharField(max_length = 200,default='linkedin')
    website      = models.CharField(max_length = 200,default='website')


class MentorConnectDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class MentorClinicDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class GlobalMarketConnectDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class DemodayDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class StateGovernmentFundingDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class CentralGovernmentFundingDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class AngelInvestorsDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class VentureCapitalistDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class angelInvestorDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class new_venturesDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class stateGovtFunddb(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 


class WhoAreWe(models.Model):
    id              = models.IntegerField(primary_key=True)
    SubHeading   = models.CharField(max_length = 2000)
    Point1   = models.CharField(max_length = 2000)
    Point2   = models.CharField(max_length = 2000)
    Point3   = models.CharField(max_length = 2000)
    Point4   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='WhoAreWe/%Y/%m/%d',default='carrer/Screenshot_3.png')
    
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.SubHeading 

class HOME_TESTIMONIAL(models.Model):
    id              = models.IntegerField(primary_key=True)
    Testimonial_content   = models.CharField(max_length = 2000)
    Name   = models.CharField(max_length = 2000)
    Designation   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='HOME_TESTIMONIAL/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Testimonial_content

class Contact_SECTION(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    Address   = models.CharField(max_length = 2000)
    Phone_number   = models.CharField(max_length = 2000)
    E_Mail           = models.ImageField(upload_to='HOME_TESTIMONIAL/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Title


class Investors(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Title

class International_Partners(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Title

class Govt_Tie(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Title

class UploadImage(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    content   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Title


class MBADB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Content 

class OurStartup(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_heading = models.CharField(max_length = 200)
    Name = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='OurStartup/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class HowWeWork(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    Point_4 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='HowWeWork/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)


class LastContent(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_heading = models.CharField(max_length = 200)
    para_1 = models.CharField(max_length = 200)
    para_2 = models.CharField(max_length = 200)
    heading_1 = models.CharField(max_length = 200)
    sub_para_1 = models.CharField(max_length = 200)
    heading_2 = models.CharField(max_length = 200)
    sub_para_2 = models.CharField(max_length = 200)
    heading_3 = models.CharField(max_length = 200)
    sub_para_3 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='LastContent/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class AboutHeading(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_heading = models.CharField(max_length = 200)
    Detail_text = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class GlobalMarket(models.Model):
    id = models.IntegerField(primary_key=True)
    Heading = models.CharField(max_length = 200)
    Content = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class GlobalMarketPic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='GlobalMarketPic/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class TOPSECTION(models.Model):
    id = models.IntegerField(primary_key=True)
    Heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='GlobalMarketPic/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class WhatWeDo(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_Heading = models.CharField(max_length = 200)
    Para_below_heading = models.CharField(max_length = 200)
    para_27 = models.CharField(max_length = 200)
    Secure_Payment_para = models.CharField(max_length = 200)
    Daily_Update_para = models.CharField(max_length = 200)
    Market_Research_para = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class OurProcess(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    concept_para = models.CharField(max_length = 200)
    prepare_para = models.CharField(max_length = 200)
    retouch_para = models.CharField(max_length = 200)
    video_link = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class SpendingSection(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    Para_below_heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    Point_4 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='GlobalMarketPic/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class JoinOurCommunity(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    Completed_Projects = models.CharField(max_length = 200)
    Satisfied_customers = models.CharField(max_length = 200)
    Expert_Employees = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class DemoDayTOPSECTION(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    Content = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class DemoDayTOPSECTION(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    Content = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class DemoDayPic(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='DemoDayPic/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class StateGovtFund(models.Model):
    id = models.IntegerField(primary_key=True)
    Main_Heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class StateGovtFundSecondSection(models.Model):
    id = models.IntegerField(primary_key=True)
    Main_Heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='StateGovtFundSecondSection/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class StateGovtFundEligibilitySection(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_Heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class Start_UpTN(models.Model):
    id = models.IntegerField(primary_key=True)
    Heading = models.CharField(max_length = 200)
    Content_1 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class Start_UpTNContent2(models.Model):
    id = models.IntegerField(primary_key=True)
    Content_2 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class Start_UpTNimg1(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Start_UpTNimg1/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class Start_UpTNimg2(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Start_UpTNimg2/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class SamridthFund(models.Model):
    id = models.IntegerField(primary_key=True)
    Main_Heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Start_UpTNimg2/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class MeitY_SAMRIDH(models.Model):
    id = models.IntegerField(primary_key=True)
    Main_Heading = models.CharField(max_length = 200)
    Point_1 = models.CharField(max_length = 200)
    Point_2 = models.CharField(max_length = 200)
    Point_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class BundledServices (models.Model):
    id = models.IntegerField(primary_key=True)
    Heading_1 = models.CharField(max_length = 200)
    Content_1 = models.CharField(max_length = 200)
    Heading_2 = models.CharField(max_length = 200)
    Content_2 = models.CharField(max_length = 200)
    Heading_3 = models.CharField(max_length = 200)
    Content_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class EDI_TOPSECTION(models.Model):
    id = models.IntegerField(primary_key=True)
    Heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='EDI_TOPSECTION/%Y/%m/%d',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)

class EDI_Overview_Section(models.Model):
    id = models.IntegerField(primary_key=True)
    point_1 = models.CharField(max_length = 200)
    point_2 = models.CharField(max_length = 200)
    point_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class EDI_InnovationVoucher(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length = 200)
    Sub_Heading = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class EDI_WeAimAtSection(models.Model):
    id = models.IntegerField(primary_key=True)
    point_1 = models.CharField(max_length = 200)
    point_2 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class EDI_Eligibility_Section(models.Model):
    id = models.IntegerField(primary_key=True)
    Sub_Heading = models.CharField(max_length = 200)
    point_1 = models.CharField(max_length = 200)
    point_2 = models.CharField(max_length = 200)
    point_3 = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class fishieries(models.Model):
    L_id = models.IntegerField(primary_key=True)
    Reson = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='logo',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)
    class Meta:
          get_latest_by = ['image']

class ContactEditPage(models.Model):
    id = models.IntegerField(primary_key=True)
    TextonImage = models.CharField(max_length = 200)
    SubHeading = models.CharField(max_length = 200)
    Address = models.CharField(max_length = 200)
    PhoneNumber = models.CharField(max_length = 200)
    mail = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)


class FooterEditPage(models.Model):
    id = models.IntegerField(primary_key=True)
    InstituteName = models.CharField(max_length = 200)
    Address = models.CharField(max_length = 200)
    PhoneNumber = models.CharField(max_length = 200)
    EXN = models.CharField(max_length = 200)
    mail = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

class SocialMediaLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    Twitter = models.CharField(max_length = 200)
    Facebook = models.CharField(max_length = 200)
    Instagram = models.CharField(max_length = 200)
    LinkedIn = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now)

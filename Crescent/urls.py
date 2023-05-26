"""Crescent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from base import views
from django.urls import path
from Crescent import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home),
    path('image_upload_page_gallery',views.image_upload_page_gallery),

    path('admin_home',views.admin_home),
    path('admin_home_auth',views.admin_home_auth),
    path('logout_admin',views.logout_admin),
    path('FourNotFout',views.FourNotFout),

    path('upload_image',views.upload_image),
    path('delete_image',views.delete_image),
    
    path('team',views.aboutus),
    path('admin_team',views.admin_team),
    path('update_team',views.update_team),
    path('delete_team',views.delete_team),

    path('birac',views.birac),
    path('birac_edit',views.birac_edit),
    path('birac_save',views.birac_save),
    path('delete_birac',views.delete_birac),
    path('set_birac',views.set_birac),
    path('facilities_developed_save',views.facilities_developed_save),
    path('delete_facilities_developed',views.delete_facilities_developed),



    path('logo',views.update_logo),
    path('upload_logo',views.upload_logo),
    path('delete_logo',views.delete_logo),
    path('set_logo',views.set_logo),

    path('carrer',views.carrer),
    path('update_carrer',views.update_carrer),
    path('edit_eventform',views.edit_eventform),


    path('eventform',views.eventform),
    path('update_eventform',views.update_eventform),
    path('delete_form',views.delete_form),


    path('convert_excel',views.convert_excel),
    path('carrer_convert_excel',views.carrer_convert_excel), # >>>>>>>>>>>>>>>>>>>>>>>> Download Files >>>>>>>>>>>>>>>>>>>>
    
    
    path('list_blog',views.list_blog),
    path('list_edit_blog',views.list_edit_blog),
    path('view_blog/<str:pk>',views.view_blog),
    path('edit_blog/<str:pk>',views.edit_blog),
    path('blog_edit',views.blog_edit),
    path('save_blog',views.save_blog),
    path('delete_blog',views.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',views.save_edit_blog),

    path('testimonicals',views.Testimonicals),
    path('testimonicals_edit',views.Testimonicals_edit),
    path('testimonicals_save',views.Testimonicals_save),

    path('events',views.events),
    path('events_save',views.events_save),
    path('events_edit',views.events_edit),

    path('tbi',views.tbi),
    path('tbi_edit',views.tbi_edit),
    path('tbi_save',views.tbi_save),
    path('delete_tbi',views.delete_tbi),
    path('set_tbi',views.set_tbi),

    path('sisfs',views.sisfs),
    path('sisfs_edit',views.sisfs_edit),
    path('sisfs_save',views.sisfs_save),
    path('delete_sisfs',views.delete_sisfs),
    path('set_sisfs',views.set_sisfs),
    path('SISFS_scheme_save',views.SISFS_scheme_save),
    path('delete_SISFS_scheme',views.delete_SISFS_scheme),


    path("about",views.about),
    path("about_edit",views.about_edit),
    
    path("EDI",views.EDI),
    path("Home",views.home),
    
    path("Mentor_Connect",views.MentorConnect),
    path("Mentor_Connect_edit",views.MontorConnect_edit),
    path("Mentor_Connect_save",views.MontorConnect_save),

    path("MBA",views.MBA),
    path("MBA_edit",views.MBA_edit),
    path("MBA_save",views.MBA_save),

    path("Mentor_Clinic",views.MentorClinic),
    path("Mentor_Clinic_edit",views.Mentor_Clinic_edit),
    path("Mentor_Clinic_save",views.Mentor_Clinic_save),

    path("angelInvestor",views.angelInvestor),
    path("angelInvestor_edit",views.angelInvestor_edit),
    path("angelInvestor_save",views.angelInvestor_save),

    path("new_ventures",views.new_ventures),
    path("new_ventures_edit",views.new_ventures_edit),
    path("new_ventures_save",views.new_ventures_save),

    path("CentralGovernmentFunding",views.CentralGovernmentFunding),
    path("CentralGovernmentFunding_edit",views.CentralGovernmentFunding_edit),
    path("CentralGovernmentFunding_save",views.CentralGovernmentFunding_save),

    path("ourstartups",views.ourStartups),
    path("ourStartups_edit",views.ourStartups_edit),
    path("ourStartups_save",views.ourStartups_save),
    path("delete_startup",views.delete_startup),
    
    path("sisfs",views.sisfs),
    path("testimonial",views.testimonial),
     
    path("career",views.career),
    path("gallery",views.gallery),

    path("home_edit",views.home_edit),
    path("whoweare_save",views.Whoweare),
    path("Home_TESTIMONIAL",views.Home_TESTIMONIAL),
    path("Contact_Section",views.Contact_Section),
    path("investors",views.investors),
    path("International_Partners",views.International),
    path("Govt_Tie",views.GovtTie),
    path("upload_images",views.Upload_Image),
    path("delete_upload",views.delete_upload),
    path("delete_investors",views.delete_investors),
    path("delete_Govt_Tie",views.delete_Govt_Tie),
    path("delete_Internationalpartners",views.delete_Internationalpartners),

    path("HowWeWork_save",views.HowWeWork_save),
    path("Last_content_save",views.Last_content_save),
    path("About_heading_save",views.About_heading_save),
    
    path("service",views.service),
    path("service_edit",views.service_edit),
    path("TopSection_save",views.TopSection_save),
    path("WhatWedo_save",views.WhatWedo_save),
    path("Our_Process_save",views.Our_Process_save),
    path("Spending_Section_save",views.Spending_Section_save),
    path("Join_Our_Community_save",views.Join_Our_Community_save),



    path("globalMarket",views.Global_Market),
    path("GlobalMarket_edit",views.GlobalMarket_edit),
    path("GlobalMarket_save",views.GlobalMarket_save),
    path("GlobalMarketPic_save",views.GlobalMarketPic_save),
    path("set_GlobalMarketPic",views.set_GlobalMarketPic),
    path("delete_GlobalMarketPic",views.delete_GlobalMarketPic),

    path("demoday",views.demoday),
    path("demoday_edit",views.demoday_edit),
    path("DemoDayTOPSECTION_save",views.DemoDayTOPSECTION_save),
    path("DemoDayPic_save",views.DemoDayPic_save),
    path("set_DemoDayPic",views.set_DemoDayPic),
    path("delete_DemoDayPic",views.delete_DemoDayPic),

    path("stategovtfunds",views.stategovtfunds),
    path("stategovtfunds_edit",views.stategovtfunds_edit),
    path("StateGovtFund_save",views.StateGovtFund_save),
    path("StateGovtFundSecondSection_save",views.StateGovtFundSecondSection_save),
    path("StateGovtFundEligibilitySection_save",views.StateGovtFundEligibilitySection_save),

    path("startuptn",views.startuptn),
    path("startuptn_edit",views.startuptn_edit),
    path("Start_UpTN_save",views.Start_UpTN_save),
    path("Start_UpTNContent2_save",views.Start_UpTNContent2_save),
    path("Start_UpTNimg1_save",views.Start_UpTNimg1_save),
    path("Start_UpTNimg2_save",views.Start_UpTNimg2_save),
 
    path("samridth",views.samridth),
    path("samridth_edit",views.samridth_edit),
    path("SamridthFund_save",views.SamridthFund_save),
    path("MeitY_SAMRIDH_save",views.MeitY_SAMRIDH_save),
    path("BundledServices_save",views.BundledServices_save),

    path("edi",views.edi),
    path("edi_edit",views.edi_edit),
    path("EDI_TOPSECTION_save",views.EDI_TOPSECTION_save),
    path("EDI_Overview_Section_save",views.EDI_Overview_Section_save),
    path("EDI_InnovationVoucher_save",views.EDI_InnovationVoucher_save),
    path("EDI_WeAimAtSection_save",views.EDI_WeAimAtSection_save),
    path("EDI_Eligibility_Section_save",views.EDI_Eligibility_Section_save),

    path('fishieriespage',views.fishieriespage),
    path('fishieries',views.update_fishieries),
    path('upload_fishieries',views.upload_fishieries),
    path('delete_fishieries',views.delete_fishieries),
    path('set_fishieries',views.set_fishieries),

    path('contact_edit',views.contact_edit),
    path('ContactEditPage_save',views.ContactEditPage_save),
    path('contact',views.contact),

    path('footer_edit',views.footer_edit),
    path('FooterEditPage_save',views.FooterEditPage_save),
    path('SocialMediaLinks_save',views.SocialMediaLinks_save),



]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
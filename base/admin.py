from django.contrib import admin

# Register your models here.
from .models import (Gallery,Team,logo,Carrer,blog,Testimonials,Events,HowWeWork,Birac,Tbi,DemoDayTOPSECTION,DemoDayPic,CentralGovernmentFundingDB,
                    ContactEditPage,fishieries,EDI_TOPSECTION,SamridthFund,Start_UpTN,StateGovtFund,OurStartup,Investors,AboutHeading,MBADB,Govt_Tie,LastContent,UploadImage,GlobalMarket,GlobalMarketPic,stateGovtFunddb,
                    FooterEditPage,SocialMediaLinks,EDI_Overview_Section,MeitY_SAMRIDH,Start_UpTNContent2,StateGovtFundSecondSection,International_Partners,Sisfs,WhoAreWe,Contact_SECTION,HOME_TESTIMONIAL,EventsForm,Facilities_developed,About_SISFS,
                    EDI_InnovationVoucher,EDI_WeAimAtSection,EDI_Eligibility_Section,BundledServices,Start_UpTNimg1,Start_UpTNimg2,StateGovtFundEligibilitySection,MentorConnectDB,MentorClinicDB, angelInvestorDB, new_venturesDB,TOPSECTION,WhatWeDo,OurProcess,SpendingSection,JoinOurCommunity)

DBobj = [Gallery,Team,logo,Carrer,blog,Testimonials,Events,HowWeWork,Birac,Tbi,DemoDayTOPSECTION,DemoDayPic,CentralGovernmentFundingDB,
                    ContactEditPage,fishieries,EDI_TOPSECTION,SamridthFund,Start_UpTN,StateGovtFund,OurStartup,Investors,AboutHeading,MBADB,Govt_Tie,LastContent,UploadImage,GlobalMarket,GlobalMarketPic,stateGovtFunddb,
                    FooterEditPage,SocialMediaLinks,EDI_Overview_Section,MeitY_SAMRIDH,Start_UpTNContent2,StateGovtFundSecondSection,International_Partners,Sisfs,WhoAreWe,Contact_SECTION,HOME_TESTIMONIAL,EventsForm,Facilities_developed,About_SISFS,
                    EDI_InnovationVoucher,EDI_WeAimAtSection,EDI_Eligibility_Section,BundledServices,Start_UpTNimg1,Start_UpTNimg2,StateGovtFundEligibilitySection,MentorConnectDB,MentorClinicDB, angelInvestorDB, new_venturesDB,TOPSECTION,WhatWeDo,OurProcess,SpendingSection,JoinOurCommunity]

for i in DBobj:
    admin.site.register(i)


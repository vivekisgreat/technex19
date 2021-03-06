from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from Auth.views import *

app_name='Auth'

urlpatterns = [

	#JsonResponse
	#url(r'^api/login/$', ApiLoginView, name= 'api_login'),
	#JsonResponse
	#url(r'^api/register/$', ApiRegisterView, name='api_register'),
	#url(r'^api/eventApi/$', eventApi, name='eventApi'),
	#url(r'^api/logout/$', logoutApi, name='logoutApi'),
	#url(r'^api/eventData/$', eventData, name='eventData'),
	#url(r'^api/parentEvents/$', parentEvents, name='parentEvents'),
	url(r'^register/$', register, name='register'),
	url(r'^login/$', loginView, name='login'),
	url(r'^events/$', events, name='event'),
	url(r'^events/(?P<key>[\w\-]+)/$', event, name='events'),
	url(r'^dashboard/$', genetella,name='dashboard'),
	#url(r'^logout/$', logoutView,name='logout'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/register'}),
	url(r'^fbConnect/$', fbConnect,name='fbConnect'),
	url(r'^resetPass/(?P<key>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^$',IndexView,name='home'),
	url(r'^lite/$',liteversion,name = 'liteversion'),
	url(r'^talks/', guestLecture, name='guestLecture'),
	url(r'^contacts/',team,name='teamPage'),
	url(r'^checkEmail/',emailUnique,name='emailUnique'),
	url(r'^botApi/',botApi,name='botApi'),
	url(r'^sponsors/',sponsors,name='sponsors'),
	url(r'^ca/',ca,name='ca'),
	#url(r'^dashboardDummy/', dummyDashboard, name='Apparent Dashboard'),
	url(r'^forgotPassword/$',forgotPassword, name='forgot Password'),

	url(r'^resetPass/(?P<forgotPassKey>[\w\-]+)/$', resetPass, name='resetPass'),
	url(r'^cdncheck/$', cdncheck, name='cdncheck'),
	url(r'^updateProfile/',profileData,name='profile edit'),
    url(r'^resetpassword/',changePass,name='change password'),
    url(r'^startupregister/',startUpRegistration,name='startup registeration'),
    url(r'^startupfair/',startupFair,name='startup Fair'),
    url(r'^hospitality/',hospitality, name='hospitality'),
    url(r'^workshopRegister/',workshopRegister,name='workshopRegister'),
    url(r'^botTest/',botTest,name='bot Test'),
    url(r'^workshops/',workshop,name='WorkShop'),
    url(r'^data/',registrationData,name='data'),
    url(r'^publicity/',publicity,name='publicity'),
    url(r'^regtrack/', regtrack , name='regtrack'),
    url(r'^dpbx/',dropboxtest,name='dpbxs'),
    url(r'^uptry/',uploadtry, name='pldlds'),
    url(r'^payment',paymentApi,name='paymentApi'),
    url(r'^theteam', fbReach, name='promotion'),
    url(r'^numberCopy/$',phoneNumberSepartion,name='Number Separator'),
    url(r'^separate/',phoneSep,name='phoneSep'),
	url(r'^exhibitions/$',exhibitions,name='exhibitions'),
	url(r'^corporate-conclave/$',corporateConclave, name='corporateConclave'),
	url(r'^send_sms/$',sendSms, name='sendSms'),
	#url(r'^quizRegister/$',quizRegister,name = 'quizRegistration'),
	url(r'^statewise/',statewise,name = 'statewise'),
	url(r'^dhoka/',dhokebaaj,name = 'dhokewale'),
	url(r'^startquiz/',startQuiz,name='startquiz'),
	url(r'^registerResponse/',registerResponse,name='registerResponse'),
	#url(r'^quizRegister2/$',quizRegister2,name = 'quizRegistration'),
	url(r'^intellecx/',quizRegister2 , name= 'test'),
	url(r'^finishQuiz/(?P<responseKey>[\w\-]+)/$',finishQuiz,name='finishQuiz'),
	url(r'^playQuiz/(?P<quizKey>[\w\-]+)/$', quizPlay, name='playQuiz'),
	url(r'^(?i)StayTechnexed/$', stayTechnexed,name='stayTechnexed'),
	url(r'^watermark/$', watermark,name='watermark'),
	url(r'feeds/$',posts,name='feeds'),
	url(r'airshow/$',airshow, name='airshow'),
	url(r'finalImage/$',finalImage,name='finalImage'),
	url(r'notificationRead/$', read, name='notificationread'),
	url(r'tshirtinfo/$', tshirt , name = 'tshirtinfo'),
	url(r'kaleidoscope/$', kaleidoscope, name="kaleidoscope"),
	url(r'slowConnection/$',slowConnection,name='slowConnection'),
	url(r'coreteam/$',coreteam,name='coreteams'),
	url(r'app/$',applink,name='applink'),

	# url(r'^quiz/$',quizI, name='quiz'),
	#url(r'^genetella/',genetella, name='Mission Dashboard'),
	#url(r'^fb/$',demofb_id,name='demofb_id'),
	# url(r'^collegejson/$', CollegeSearch, name='api_register'),
	#url(r'^$', IndexView, name= 'index'),

	#url(r'^logout/$', LogoutView, name='logout'),
	url(r'^googlec0c9e6f96a842b6d.html/',gverify,name='gverify'),

]

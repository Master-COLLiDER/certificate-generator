from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('certificate.views',
    # Examples:
    # url(r'^$', 'fossee_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', name='index'),
    url(r'^download/$', 'download', name='download'),
    url(r'^verify/$', 'verify', name='verify'),
    url(r'^verify/(?P<serial_key>.*)/$', 'verify', name='verify-directly'),
    url(r'^feedback/$', 'feedback', name='feedback'),
    url(r'^scipy_feedback/$', 'scipy_feedback', name='scipy_feedback'),
    url(r'^scipy_feedback_2015/$', 'scipy_feedback_2015', name='scipy_feedback_2015'),
    url(r'^scipy_feedback_2016/$', 'scipy_feedback_2016', name='scipy_feedback_2016'),
    url(r'^openmodelica_feedback_2017/$', 'openmodelica_feedback_2017', name='openmodelica_feedback_2017'),
    url(r'^openmodelica_download_2017/$', 'openmodelica_download_2017', name='openmodelica_download_2017'),
    url(r'^python_workshop_download/$', 'python_workshop_download', name='python_workshop_download'),
    url(r'^python_certificate/$', 'python_certification_download', name='python_certification_download'),
    url(r'^python_workshop_feedback/$', 'python_workshop_feedback', name='python_workshop_feedback'),
    url(r'^drupal_feedback/$', 'drupal_feedback', name='drupal_feedback'),
    url(r'^dwsim_feedback/$', 'dwsim_feedback', name='dwsim_feedback'),
    url(r'^arduino_feedback/$', 'arduino_feedback', name='arduino_feedback'),
    url(r'^arduino_google_feedback/$', 'arduino_google_feedback', name='arduino_google_feedback'),
    url(r'^scipy_download/$', 'scipy_download', name='scipy_download'),
    url(r'^drupal_download/$', 'drupal_download', name='drupal_download'),
    url(r'^tbc_freeeda_download/$', 'tbc_freeeda_download', name='tbc_freeeda_download'),
    url(r'^dwsim_download/$', 'dwsim_download', name='dwsim_download'),
    url(r'^arduino_download/$', 'arduino_download', name='arduino_download'),
    url(r'^esim_download/$', 'esim_download', name='esim_download'),
    url(r'^esim_google_feedback/$', 'esim_google_feedback', name='esim_google_feedback'),
    url(r'^osdag_workshop_download/$', 'osdag_workshop_download', name='osdag_workshop_download'),
    url(r'^osdag_workshop_feedback/$', 'osdag_workshop_feedback', name='osdag_workshop_feedback'),
    url(r'^esim_workshop_download/$', 'esim_workshop_download', name='esim_workshop_download'),
    url(r'^esim_workshop_feedback/$', 'esim_workshop_feedback', name='esim_workshop_feedback'),
    url(r'^scipy_download_2015/$', 'scipy_download_2015', name='scipy_download_2015'),
    url(r'^scipy_download_2016/$', 'scipy_download_2016', name='scipy_download_2016'),
    url(r'^openfoam_symposium_download_2016/$', 'openfoam_symposium_download_2016', name='openfoam_symposium_download_2016'),
    url(r'^openfoam_symposium_feedback_2016/$', 'openfoam_symposium_feedback_2016', name='openfoam_symposium_feedback_2016'),
    url(r'^fossee_internship_cerificate_download/$', 'fossee_internship16_cerificate_download', name='fossee_internship_cerificate_download'),
    url(r'^drupal_workshop_download/$', 'drupal_workshop_download', name='drupal_workshop_download'),
    url(r'^scipy_download_2017/$', 'scipy_download_2017', name='scipy_download_2017'),
    url(r'^scipy_feedback_2017/$', 'scipy_feedback_2017', name='scipy_feedback_2017'),
    url(r'^scipy_download_2018/$', 'scipy_download_2018', name='scipy_download_2018'),
    url(r'^scipy_feedback_2018/$', 'scipy_feedback_2018', name='scipy_feedback_2018'),
    url(r'^scipy_download_2019/$', 'scipy_download_2019', name='scipy_download_2019'),
    url(r'^scipy/$', 'scipy_all_download', name='scipy_all_download'),
    url(r'^scipy/(?P<year>.*)/$', 'scipy_all_download', name='scipy_all_download_2021'),
    url(r'^complex-fluids/$', 'complex_fluids_download', name='complex_fluids_download'),
    url(r'^scipy_feedback_2019/$', 'scipy_feedback_2019', name='scipy_feedback_2019'),
    url(r'^python_workshop_download/contact$', 'contact', name='contact'),
    url(r'^nccps_feedback_2018/$', 'nccps_feedback_2018', name='nccps_feedback_2018'),
    url(r'^nccps_download_2018/$', 'nccps_download_2018', name='nccps_download_2018'),
    url(r'^st_feedback_2019/$', 'st_feedback_2019', name='st_feedback_2019'),
    url(r'^st_workshop_download/$', 'st_workshop_download', name='st_workshop_download'),
    url(r'^pymain_workshop_download/$', 'pymain_workshop_download', name='pymain_workshop_download'),
    url(r'^linuxcoord_workshop_download/$', 'linuxcoord_workshop_download', name='linuxcoord_workshop_download'),
    url(r'^esimcoord_workshop_download/$', 'esimcoord_workshop_download', name='esimcoord_workshop_download'),
    url(r'^scilabsupport_workshop_download/$', 'scilabsupport_workshop_download', name='scilabsupport_workshop_download'),
    url(r'^pythonsupport_workshop_download/$', 'pythonsupport_workshop_download', name='pythonsupport_workshop_download'),
    url(r'^linuxsupport_workshop_download/$', 'linuxsupport_workshop_download',
        name='linuxsupport_workshop_download'),
    url(r'^esimsupport_workshop_download/$', 'esimsupport_workshop_download',
        name='esimsupport_workshop_download'),
    url(r'^cppsupport_workshop_download/$', 'cppsupport_workshop_download',
        name='cppsupport_workshop_download'),
    url(r'^ardsupport_workshop_download/$', 'ardsupport_workshop_download',
        name='ardsupport_workshop_download'),
    url(r'^rsupport_workshop_download/$', 'rsupport_workshop_download',
        name='rsupport_workshop_download'),
    url(r'^foss_workshop_test_download/$', 'foss_workshop_test_download',
        name='foss_workshop_test_download'),
    url(r'^fellowship2019_certificate_download/$', 'fellowship2019_certificate_download', name='fellowship2019_certificate_download'),
    url(r'^fellowship_certificate/2020/$', 'fellow20_certificate_download',
        name='fellow20_certificate_download'),
    url(r'^fellowship/2021/$', 'fellow21_certificate_download',
        name='fellow21_certificate_download'),
    url(r'^internship_certificate/2020/$', 'intern20_certificate_download',
        name='intern20_certificate_download'),
    url(r'^internship_certificate/2021/$', 'intern21_certificate_download',
        name='intern21_certificate_download'),
    url(r'^eqfellowship2019_certificate_download/$', 'eqfellowship2019_certificate_download', name='eqfellowship2019_certificate_download'),
    url(r'^osdag2019_certificate_download/$', 'osdag2019_certificate_download', name='osdag2019_certificate_download'),
    url(r'^animation_certificate_download/$', 'animation_certificate_download',
        name='animation_certificate_download'),
    url(r'^animation/internship_certificate/$', 'animation_internship_certificate_download',
        name='animation_internship_certificate_download'),
    url(r'^animation/contribution_certificate/$', 'animation_contribution_certificate_download',
        name='animation_contribution_certificate_download'),
    url(r'^winter_internship_certificate_download/$', 'winter_internship_certificate_download',
        name='winter_internship_certificate_download'),
    url(r'^fdp_certificate_download/$', 'fdp_certificate_download',
        name='fdp_certificate_download'),
    url(r'^openfoam/$', 'openfoam_certificate_download',
        name='openfoam_certificate_download'),
    url(r'^synfig_hackathon/$', 'synfig_hackathon_certificate_download',
        name='synfig_hackathon_certificate_download'),
    url(r'^mapathon/$', 'mapathon_certificate_download',
        name='mapathon_certificate_download'),
    url(r'^mapathon/2022/$', 'mapathon2_certificate_download',
        name='mapathon2_certificate_download'),
    url(r'^esim/marathon/$', 'esim_marathon_certificate_download',
        name='esim_marathon_certificate_download'),
    url(r'^esim/marathon/2022$', 'esim_marathon_2022_certificate_download',
        name='esim_marathon_2022_certificate_download'),
    url(r'^hackathon/scilab/$', 'hackathon_certificate_download',
        name='hackathon_certificate_download'),
    url(r'^vlab/$', 'vlabappre_certificate_download',
        name='vlabappre_certificate_download'),
    url(r'^r/$', 'rappre_certificate_download',
        name='rappre_certificate_download'),
    url(r'^python/$', 'python_certified_students',
        name='python_certified_students'),
    url(r'^python_csv/$', 'certified_csv',
        name='certified_csv'),
)

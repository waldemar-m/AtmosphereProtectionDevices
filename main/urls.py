from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^centrifugal_pump/result/$','wyswietl.views.centrifugal_pump_result'),
    url(r'^centrifugal_pump/form/$','wyswietl.views.centrifugal_pump_form'),
    url(r'^$','wyswietl.views.index'),
    url(r'^boiler/forms/$','wyswietl.views.boiler_forms'),
    url(r'^boiler/result/$','wyswietl.views.boiler_result'),
    url(r'^electrostatic_precipitators/form/$','wyswietl.views.electrostatic_form'),
    url(r'^electrostatic_precipitators/result/$','wyswietl.views.electrostatic_result'),
    url(r'^scr_reactor_nox/form/$', 'wyswietl.views.scr_form'),
    url(r'^scr_reactor_nox/result/$', 'wyswietl.views.scr_result')
)

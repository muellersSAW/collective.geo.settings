from zope.interface import implementer
#from plone.base.interfaces import IConfigurationChangedEvent
#from plone.app.controlpanel.interfaces import IConfigurationChangedEvent
from Products.CMFPlone.interfaces import IConfigurationChangedEvent
from Products.CMFPlone.controlpanel.events import ConfigurationChangedEvent


class IGeoSettingsEvent(IConfigurationChangedEvent):
    """An event signaling that geo settings are saved
    """

@implementer(IGeoSettingsEvent)
class GeoSettingsEvent(ConfigurationChangedEvent):
   pass 

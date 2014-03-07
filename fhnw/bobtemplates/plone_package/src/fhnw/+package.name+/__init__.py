from AccessControl import ModuleSecurityInfo
from zope.i18nmessageid import MessageFactory

FHNWSocialMediaMessageFactory = MessageFactory('fhnwsocialmedia')
ModuleSecurityInfo('fhnw.socialmedia').declarePublic('FHNWSocialMediaMessageFactory')

from AccessControl import ModuleSecurityInfo
from zope.i18nmessageid import MessageFactory

FHNWSocialMediaMessageFactory = MessageFactory('fhnw{{{package.name}}}')
ModuleSecurityInfo('fhnw.{{{package.name}}}'
    ).declarePublic('FHNWSocialMediaMessageFactory')

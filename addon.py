import xbmcaddon
import xbmc
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
url = 'http://streymi.skjarinn.is/Skjarinn/smil:SkjarEinn/playlist.m3u8'

xbmc.Player().play(url, xbmcgui.ListItem(addonname))

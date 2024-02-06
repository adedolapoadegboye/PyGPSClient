"""
strings.py

ENGLISH language string literals for PyGPSClient application

Created on 12 Sep 2020

:author: semuadmin
:copyright: SEMU Consulting © 2020
:license: BSD 3-Clause
"""

# pylint: disable=line-too-long

TITLE = "PyGPSClient"

COPYRIGHTTXT = "\u00A9 SEMU Consulting 2020\nBSD-2 License. All Rights Reserved"

INTROTXT = "Welcome to PyGPSClient!"
INTROTXTNOPORTS = "Welcome to PyGPSClient!"

HELPTXT = "Help..About - display About dialog."

ABOUTTXT = (
    "PyGPSClient is a free, open-source GNSS/GPS diagnostic and configuration "
    + "application written entirely in Python and tkinter. "
    + "It supports NMEA, UBX, RTCM3, NTRIP & SPARTN protocols. "
    + "Instructions and source code are available on GitHub at the link below."
)
NA = "N/A"

MAPAPIURL = "https://developer.mapquest.com/user/login/sign-up"

# Message text
BADJSONERROR = "ERROR! Invalid metadata file"
CONFIGBAD = "{} command rejected"
CONFIGERR = "Invalid configuration data"
CONFIGOK = "{} command accepted"
CONFIGRXM = "{} polled, {} key(s) loaded"
CONFIGTITLE = "Config File"
ENDOFFILE = "End of file reached"
FILEOPENERROR = "Error opening file {}"
INACTIVE_TIMEOUT = "Inactivity timeout"
LOADCONFIGBAD = "Configuration not loaded {} {}, using defaults"
LOADCONFIGOK = "Configuration loaded {}"
LOADCONFIGNONE = "Configuration file not found {}, using defaults"
MQTTCONN = "Connecting to MQTT server {}..."
NMEAVALERROR = "Value error in NMEA message: {}"
NOTCONN = "Not connected"
NOWEBMAP = "Unable to display map."
NOWEBMAPCONN = NOWEBMAP + "\nCheck internet connection."
NOWEBMAPFIX = NOWEBMAP + "\nNo satellite fix."
NOWEBMAPHTTP = NOWEBMAP + "\nBad HTTP response: {}.\nCheck MQAPIKEY.\n"
NOWEBMAPKEY = NOWEBMAP + f"\nMQAPIKEY not found or invalid.\n\n{MAPAPIURL}"
NULLSEND = "Nothing to send"
OPENFILEERROR = "ERROR! File could not be opened"
READTITLE = "Select File"
SAVECONFIGBAD = "Configuration not saved {}"
SAVECONFIGOK = "Configuration saved OK"
SAVEERROR = "ERROR! File could not be saved to specified directory"
SAVETITLE = "Select Directory"
SEROPENERROR = "Error opening serial port {}"
SETINITTXT = "Settings initialised"
STOPDATA = "Serial reader process stopped"
UBXPOLL = "Polling current UBX configuration..."
VALERROR = "ERROR! Please correct highlighted entries"
VERCHECK = "Newer version of PyGPSClient available: {}"
WAITNMEADATA = "Waiting for data..."
WAITUBXDATA = "Waiting for data..."
NOWDGSWARN = "WARNING! No widgets are enabled in config file {} - display will be blank"

# Menu text
MENUABOUT = "About"
MENUCAN = "Cancel"
MENUEXIT = "Exit"
MENUFILE = "File"
MENUHELP = "Help"
MENULOAD = "Load Configuration"
MENUOPTION = "Options"
MENURESET = "Reset Layout"
MENURST = "Reset"
MENUSAVE = "Save Configuration"
MENUVIEW = "View"


# Button text
BTNCAN = "Cancel"
BTNPLOT = "PLOT"
BTNRST = "Reset"
BTNSAVE = "Save"

# Label text
LBLACCURACY = "Accuracy (cm)"
LBLCFGGENERIC = "CFG-* Generic Configuration"
LBLCFGMSG = "CFG-MSG Message Rate Configuration"
LBLCFGPRT = "CFG-PRT Protocol Configuration"
LBLCFGRATE = "CFG-RATE Navigation Solution Rate Configuration"
LBLCFGRECORD = "CFG Configuration Load/Save/Record"
LBLCONFIGBASE = "Configure Base Station"
LBLCTL = "Controls"
LBLDATADISP = "Console Display"
LBLDATALOG = "DataLogging"
LBLDEGFORMAT = "Position Format"
LBLDURATIONS = "Duration (s)"
LBLGGAFIXED = "Fixed Reference"
LBLGGALIVE = "Receiver"
LBLJSONLOAD = "Load Keys From JSON"
LBLLANIP = "LAN IP"
LBLNTRIPCONFIG = "NTRIP Client"
LBLNTRIPGGAINT = "GGA Interval s"
LBLNTRIPMOUNT = "Mountpoint"
LBLNTRIPPORT = "Port"
LBLNTRIPPWD = "Password"
LBLNTRIPSERVER = "Server"
LBLNTRIPSTR = "Sourcetable"
LBLNTRIPUSER = "User"
LBLNTRIPVERSION = "Version"
LBLPRESET = "Preset UBX Configuration Commands"
LBLPROTDISP = "Protocols Shown"
LBLPUBLICIP = "Public IP"
LBLSERVERHOST = "Host IP"
LBLSERVERMODE = "Mode"
LBLSERVERPORT = "Port"
LBLSET = "Settings"
LBLSHOWUNUSED = "Show Unused Satellites"
LBLSOCKSERVE = "Socket Server /\nNTRIP Caster   "  # padded to align
LBLSPARTNCONFIG = "SPARTN Client"
LBLSPARTNGN = "GNSS RECEIVER CONFIGURATION (F9*)"
LBLSPARTNIP = "IP CORRECTION CONFIGURATION (MQTT)"
LBLSPARTNLB = "L-BAND CORRECTION CONFIGURATION (D9*)"
LBLSPTNCURR = "CURRENT SPARTN KEY:"
LBLSPTNDAT = "Valid from YYYYMMDD"
LBLSPTNFP = "Configure receiver"
LBLSPTNKEY = "Key as hexadecimal"
LBLSPTNNEXT = "NEXT SPARTN KEY:"
LBLSPTNUPLOAD = "Upload keys"
LBLSTREAM = "Stream\nfrom file"
LBLTRACKRECORD = "GPX Track"
LBLUBXCONFIG = "UBX Config"
LBLUDPORT = "USER-DEFINED PORT"
LBLDISNMEA = "Disable NMEA"

# Dialog text
DLGABOUT = "PyGPSClient"
DLGENABLEMONSPAN = "Enable or poll MON-SPAN message"
DLGENABLEMONSYS = "Enable or poll MON-SYS/COMMS messages"
DLGGPXERROR = "GPX PARSING ERROR!"
DLGGPXLOAD = "LOADING GPX TRACK ..."
DLGGPXNULL = "NO TRACKPOINTS IN GPX FILE!"
DLGGPXPROMPT = "CLICK FOLDER ICON TO LOAD GPX FILE"
DLGGPXVIEWER = "GPX Track Viewer"
DLGHOWTO = "How To Use PyGPSCLient"
DLGJSONERR = "ERROR! {}"
DLGJSONOK = "Keys loaded from {}"
DLGNOMONSPAN = "This receiver does not appear to\nsupport the MON-SPAN messages"
DLGNOMONSYS = "This receiver does not appear to support\nthe MON-SYS/COMMS messages"
DLGNTRIPCONFIG = "NTRIP Client Configuration"
DLGRESET = "Confirm Reset"
DLGRESETCONFIRM = (
    "Are you sure you want to reset the\ncurrent configuration to the\nfactory default?"
)
DLGSAVE = "Confirm Save"
DLGSAVECONFIRM = "Are you sure you want to save\nthe current configuration?"
DLGSPARTNCONFIG = "SPARTN Client Configuration"
DLGSPARTNWARN = "WARNING! Disconnect from {} client before using {} client"
DLGUBXCONFIG = "UBX Configuration"
DLGWAITMONSPAN = "Waiting for MON-SPAN message..."
DLGWAITMONSYS = "Waiting for MON-SYS/COMMS messages..."
DLGSTOPRTK = "WARNING! Stop all active connections before loading configuration"

# UBX Preset Command Descriptions
PSTALLINFOFF = "CFG-INF - Turn OFF all non-error INF msgs"
PSTALLINFON = "CFG-INF - Turn ON all INF msgs"
PSTALLLOGOFF = "CFG-MSG - Turn OFF all LOG msgs"
PSTALLLOGON = "CFG-MSG - Turn ON all LOG msgs"
PSTALLMONOFF = "CFG-MSG - Turn OFF all MON msgs"
PSTALLMONON = "CFG-MSG - Turn ON all MON msgs"
PSTALLNMEAOFF = "CFG-MSG - Turn OFF all NMEA msgs"
PSTALLNMEAON = "CFG-MSG - Turn ON all NMEA msgs"
PSTALLRXMOFF = "CFG-MSG - Turn OFF all RXM msgs"
PSTALLRXMON = "CFG-MSG - Turn ON all RXM msgs"
PSTALLUBXOFF = "CFG-MSG - Turn OFF all UBX NAV msgs"
PSTALLUBXON = "CFG-MSG - Turn ON all UBX NAV msgs"
PSTMINNMEAON = "CFG-MSG - Turn ON minimum NMEA msgs"
PSTMINUBXON = "CFG-MSG - Turn ON minimum UBX NAV msgs"
PSTPOLLALLCFG = "CFG-xxx - Poll All Configuration Messages"
PSTPOLLALLNAV = "NAV(2)-xxx - Poll All Navigation Messages"
PSTPOLLINFO = "CFG-INF - Poll Info message config"
PSTPOLLPORT = "CFG-PRT - Poll Port config"
PSTRESET = "CFG-CFG - RESTORE FACTORY DEFAULTS"
PSTSAVE = "CFG-CFG - Save configuration to non-volatile memory"

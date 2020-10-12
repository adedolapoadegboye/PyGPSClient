'''
Banner frame class for PyGPSClient application.

This handles the top banner which prominently displays the current coordinates and status.

Created on 13 Sep 2020

@author: semuadmin
'''
# pylint: disable=line-too-long

from platform import system
from tkinter import Frame, Label, Button, StringVar, font, N, S, W, E, SUNKEN

from PIL import ImageTk, Image
from pyubx2 import UBXMessage

from .globals import deg2dmm, deg2dms, m2ft, kmph2mph, kmph2ms, kmph2knots, \
                                DMM, DMS, UMM, UI, UIK, ICON_CONN, ICON_DISCONN, \
                                CONNECTED, DISCONNECTED, BGCOL, FGCOL, ADVOFF, ADVON


class BannerFrame(Frame):
    '''
    Frame inheritance class for banner.
    '''

    def __init__(self, app, *args, **kwargs):
        '''
        Constructor.
        '''

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)
        Frame.__init__(self, self.__master, *args, **kwargs)

        self._time = StringVar()
        self._lat = StringVar()
        self._lon = StringVar()
        self._alt = StringVar()
        self._speed = StringVar()
        self._alt_u = StringVar()
        self._speed_u = StringVar()
        self._track = StringVar()
        self._dop = StringVar()
        self._hvdop = StringVar()
        self._hvacc = StringVar()
        self._fix = StringVar()
        self._siv = StringVar()
        self._sip = StringVar()
        self._status = False
        self._show_advanced = True

        self._bgcol = BGCOL
        self._fgcol = FGCOL
        self.config(bg=self._bgcol)
        self._img_conn = ImageTk.PhotoImage(Image.open (ICON_CONN))
        self._img_disconn = ImageTk.PhotoImage(Image.open (ICON_DISCONN))
        self.width, self.height = self.get_size()

        self._body()
        self._do_layout()
        self._attach_events()

    def _body(self):
        '''
        Set up frame and widgets.
        '''

        for i in range(2, 5):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)
        self._frm_connect = Frame(self, bg=BGCOL)
        self._frm_toggle = Frame(self, bg=BGCOL)
        self._frm_basic = Frame(self, bg=BGCOL, relief=SUNKEN)
        self._frm_advanced = Frame(self, bg=BGCOL)

        self.option_add("*Font", self.__app.font_md2)
        self._lbl_ltime = Label(self._frm_basic, text="utc:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_llat = Label(self._frm_basic, text="lat:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_llon = Label(self._frm_basic, text="lon:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lalt = Label(self._frm_basic, text="alt:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lspd = Label(self._frm_basic, text="speed:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_ltrk = Label(self._frm_basic, text="track:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._btn_toggle = Button(self._frm_toggle, text=ADVON, width=3,
                                  command=self._toggle_advanced)
        self._lbl_lfix = Label(self._frm_basic, text="fix:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lsiv = Label(self._frm_advanced, text="siv:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lsip = Label(self._frm_advanced, text="sip:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lpdop = Label(self._frm_advanced, text="pdop:", bg=self._bgcol, fg=self._fgcol, anchor=N)
        self._lbl_lacc = Label(self._frm_advanced, text="acc:", bg=self._bgcol, fg=self._fgcol, anchor=N)

        self.option_add("*Font", self.__app.font_lg)
        self._lbl_status = Label(self._frm_connect, bg=self._bgcol, image=self._img_conn, fg="blue")
        self._lbl_time = Label(self._frm_basic, textvariable=self._time, bg=self._bgcol, fg="cyan")
        self._lbl_lat = Label(self._frm_basic, textvariable=self._lat, bg=self._bgcol, fg="orange")
        self._lbl_lon = Label(self._frm_basic, textvariable=self._lon, bg=self._bgcol, fg="orange")
        self._lbl_alt = Label(self._frm_basic, textvariable=self._alt, bg=self._bgcol, fg="orange")
        self._lbl_spd = Label(self._frm_basic, textvariable=self._speed, bg=self._bgcol, fg="deepskyblue")
        self._lbl_trk = Label(self._frm_basic, textvariable=self._track, bg=self._bgcol, fg="deepskyblue")
        self._lbl_fix = Label(self._frm_basic, textvariable=self._fix, bg=self._bgcol, fg="white")
        self._lbl_siv = Label(self._frm_advanced, textvariable=self._siv, bg=self._bgcol, fg="yellow")
        self._lbl_sip = Label(self._frm_advanced, textvariable=self._sip, bg=self._bgcol, fg="yellow")
        self._lbl_pdop = Label(self._frm_advanced, textvariable=self._dop, bg=self._bgcol, fg="mediumpurple2")

        self.option_add("*Font", self.__app.font_sm)
        self._lbl_lalt_u = Label(self._frm_basic, textvariable=self._alt_u, bg=self._bgcol, fg="orange",
                                anchor=S)
        self._lbl_lspd_u = Label(self._frm_basic, textvariable=self._speed_u, bg=self._bgcol, fg="deepskyblue",
                                anchor=S)
        self._lbl_hvdop = Label(self._frm_advanced, textvariable=self._hvdop, bg=self._bgcol, fg="mediumpurple2")
        self._lbl_hvacc = Label(self._frm_advanced, textvariable=self._hvacc, bg=self._bgcol, fg="aquamarine2")
        self._lbl_lacc_u = Label(self._frm_advanced, textvariable=self._alt_u, bg=self._bgcol, fg="aquamarine2", anchor=N)

    def _do_layout(self):
        '''
        Position widgets in frame.
        '''

        self._lbl_status.grid(column=0, row=0, padx=8, pady=3, sticky=W)
        self._lbl_ltime.grid(column=1, row=0, pady=3, sticky=W)
        self._lbl_time.grid(column=2, row=0, pady=3, sticky=W)
        self._lbl_llat.grid(column=3, row=0, pady=3, sticky=W)
        self._lbl_lat.grid(column=4, row=0, pady=3, sticky=W)
        self._lbl_llon.grid(column=5, row=0, pady=3, sticky=W)
        self._lbl_lon.grid(column=6, row=0, pady=3, sticky=W)
        self._lbl_lalt.grid(column=7, row=0, pady=3, sticky=W)
        self._lbl_alt.grid(column=8, row=0, pady=3, sticky=W)
        self._lbl_lalt_u.grid(column=9, row=0, pady=0, sticky=W)
        self._lbl_lspd.grid(column=10, row=0, pady=3, sticky=W)
        self._lbl_spd.grid(column=11, row=0, pady=3, sticky=W)
        self._lbl_lspd_u.grid(column=12, row=0, pady=0, sticky=W)
        self._lbl_ltrk.grid(column=13, row=0, pady=3, sticky=W)
        self._lbl_trk.grid(column=14, row=0, pady=3, sticky=W)
        self._lbl_lfix.grid(column=15, row=0, pady=3, sticky=W)
        self._lbl_fix.grid(column=16, row=0, pady=3, sticky=W)

        self._lbl_lsiv.grid(column=0, row=0, pady=3, sticky=W)
        self._lbl_siv.grid(column=1, row=0, pady=3, sticky=W)
        self._lbl_lsip.grid(column=2, row=0, pady=3, sticky=W)
        self._lbl_sip.grid(column=3, row=0, pady=3, sticky=W)
        self._lbl_lpdop.grid(column=4, row=0, pady=3, sticky=W)
        self._lbl_pdop.grid(column=5, row=0, pady=3, sticky=W)
        self._lbl_hvdop.grid(column=6, row=0, pady=0, sticky=W)
        self._lbl_lacc.grid(column=7, row=0, pady=3, sticky=W)
        self._lbl_hvacc.grid(column=8, row=0, pady=0, sticky=W)
        self._lbl_lacc_u.grid(column=9, row=0, pady=0, sticky=W)

        self._btn_toggle.grid(column=0, row=0, padx=8, pady=3, sticky=(N, E))

        self._toggle_advanced()

    def _toggle_advanced(self):
        '''
        Toggle advanced banner frame on or off.
        '''

        self._frm_connect.grid(column=0, row=0, rowspan=2,
                               pady=3, ipadx=3, ipady=3, sticky=(N, W))
        self._frm_basic.grid(column=1, row=0, pady=3, sticky=(W))
        self._frm_toggle.grid(column=5, row=0, rowspan=2, pady=3,
                              sticky=(N, E))
        self._show_advanced = not self._show_advanced
        if self._show_advanced:
            self._frm_advanced.grid(column=1, row=1, pady=3, sticky=(W))
            self._btn_toggle.config(text=ADVON)
        else:
            self._frm_advanced.grid_forget()
            self._btn_toggle.config(text=ADVOFF)

    def _attach_events(self):
        '''
        Bind events to frame.
        '''

        self.bind("<Configure>", self._on_resize)

    def update_banner(self, **kwargs):
        '''
        Sets text of banner from keyword parms.
        '''

        settings = self.__app.frm_settings.get_settings()
        disp_format = settings['format']
        units = settings['units']

        if 'time' in kwargs:
            self._time.set(kwargs['time'])
        if 'lat' in kwargs:
            if kwargs['lat'] == '':
                self._lat.set('N/A')
            else:
                if disp_format == DMS:
                    self._lat.set(deg2dms(kwargs['lat'], 'lat'))
                elif disp_format == DMM:
                    self._lat.set(deg2dmm(kwargs['lat'], 'lat'))
                else:
                    self._lat.set(round(kwargs['lat'], 5))
        if 'lon' in kwargs:
            if kwargs['lon'] == '':
                self._lon.set('N/A')
            else:
                if disp_format == DMS:
                    self._lon.set(deg2dms(kwargs['lon'], 'lon'))
                elif disp_format == DMM:
                    self._lon.set(deg2dmm(kwargs['lon'], 'lon'))
                else:
                    self._lon.set(round(kwargs['lon'], 5))
        if 'alt' in kwargs:
            if kwargs['alt'] is None:
                self._alt.set('N/A')
                self._alt_u.set('')
            else:
                if units in (UI, UIK):
                    self._alt.set(round(m2ft(float(kwargs['alt'])), 1))
                    self._alt_u.set('ft')
                else:
                    self._alt.set(round(kwargs['alt'], 1))
                    self._alt_u.set('m')
        if 'speed' in kwargs:
            if kwargs['speed'] is None:
                self._speed.set('N/A')
                self._speed_u.set('')
            else:
                if units == UI:
                    self._speed.set(round(kmph2mph(float(kwargs['speed'])), 1))
                    self._speed_u.set('mph')
                elif units == UIK:
                    self._speed.set(round(kmph2knots(float(kwargs['speed'])), 1))
                    self._speed_u.set('knots')
                elif units == UMM:
                    self._speed.set(round(kmph2ms(float(kwargs['speed'])), 1))
                    self._speed_u.set('m/s')
                else:
                    self._speed.set(round(kwargs['speed'], 1))
                    self._speed_u.set('kmph')
        if 'track' in kwargs:
            if kwargs['track'] is None:
                self._track.set('N/A')
            else:
                self._track.set(str(round(kwargs['track'], 1)))
        if 'siv' in kwargs:
            self._siv.set(str(kwargs['siv']).zfill(2))
        if 'sip' in kwargs:
            self._sip.set(str(kwargs['sip']).zfill(2))
        if 'dop' in kwargs:
            dop = kwargs['dop']
            self._dop.set(str(dop) + " " + UBXMessage.dop2str(dop))
        if 'hdop' in kwargs and 'vdop' in kwargs:
            self._hvdop.set("hdop " + str(kwargs['hdop']) + "\nvdop " + str(kwargs['vdop']))
        if 'hacc' in kwargs and 'vacc' in kwargs:
            if units in (UI, UIK):
                hacc = round(m2ft(kwargs['hacc']), 1)
                vacc = round(m2ft(kwargs['vacc']), 1)
            else:
                hacc = round(kwargs['hacc'], 1)
                vacc = round(kwargs['vacc'], 1)
            self._hvacc.set("hacc " + str(hacc) + "\nvacc " + str(vacc))
        if 'fix' in kwargs:
            if kwargs['fix'] in ('3D', '3D + DR'):
                self._lbl_fix.config(fg="green2")
            elif kwargs['fix'] in ('2D', 'DR'):
                self._lbl_fix.config(fg="orange")
            else:
                self._lbl_fix.config(fg="red")
            self._fix.set(kwargs['fix'])
        if 'status' in kwargs:
            self._status = kwargs['status']
            if self._status == CONNECTED:
                self._lbl_status.configure(image=self._img_conn)
            else:
                self._lbl_status.configure(image=self._img_disconn)

    def _set_fontsize(self):
        '''
        Adjust font sizes according to frame size
        '''

        w = self.width
        # Cater for slightly different font behaviour on Linux
        if system() in ("W32", "Darwin"):
            val = 55
            lbl = 75
            sup = 85
        else:
            val = 70
            lbl = 85
            sup = 95

        sz = min(int(w / val), 18)
        self._lbl_status.config(font=font.Font(size=sz))
        self._lbl_time.config(font=font.Font(size=sz))
        self._lbl_lat.config(font=font.Font(size=sz))
        self._lbl_lon.config(font=font.Font(size=sz))
        self._lbl_alt.config(font=font.Font(size=sz))
        self._lbl_spd.config(font=font.Font(size=sz))
        self._lbl_trk.config(font=font.Font(size=sz))
        self._lbl_pdop.config(font=font.Font(size=sz))
        self._lbl_fix.config(font=font.Font(size=sz))
        self._lbl_sip.config(font=font.Font(size=sz))
        self._lbl_siv.config(font=font.Font(size=sz))

        sz = min(int(w / lbl), 14)
        self._lbl_ltime.config(font=font.Font(size=sz))
        self._lbl_llat.config(font=font.Font(size=sz))
        self._lbl_llon.config(font=font.Font(size=sz))
        self._lbl_lalt.config(font=font.Font(size=sz))
        self._lbl_lspd.config(font=font.Font(size=sz))
        self._lbl_ltrk.config(font=font.Font(size=sz))
        self._lbl_lpdop.config(font=font.Font(size=sz))
        self._lbl_lfix.config(font=font.Font(size=sz))
        self._lbl_lsip.config(font=font.Font(size=sz))
        self._lbl_lsiv.config(font=font.Font(size=sz))
        self._lbl_lacc.config(font=font.Font(size=sz))

        sz = min(int(w / sup), 12)
        self._lbl_lalt_u.config(font=font.Font(size=sz))
        self._lbl_lspd_u.config(font=font.Font(size=sz))
        self._lbl_hvdop.config(font=font.Font(size=sz))
        self._lbl_hvacc.config(font=font.Font(size=sz))

    def _on_resize(self, event):
        '''
        Resize frame
        '''

        self.width, self.height = self.get_size()
        self._set_fontsize()

    def get_size(self):
        '''
        Get current frame size.
        '''

        self.update_idletasks()  # Make sure we know about any resizing
        width = self.winfo_width()
        height = self.winfo_height()
        return (width, height)

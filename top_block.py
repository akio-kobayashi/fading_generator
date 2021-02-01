#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Mar 18 10:20:53 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.seed = seed = 128
        self.m_rate = m_rate = 0.8
        self.if_rate = if_rate = samp_rate*40
        self.gauss = gauss = 0
        self.fc = fc = 511e3
        self.dpp = dpp = 100.0

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=if_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_fff(
                interpolation=3,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=40,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(301, firdes.WIN_HAMMING, 6.76)
        self.channels_fading_model_0 = channels.fading_model( 8, dpp/if_rate, False, 2, 256 )
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/media/akio/ssd1/fading_generator/5-263831-B-6.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((m_rate, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-8e3, fc+8e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0 = analog.sig_source_f(if_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.wxgui_fftsink2_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.channels_fading_model_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.low_pass_filter_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_if_rate(self.samp_rate*40)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_seed(self):
        return self.seed

    def set_seed(self, seed):
        self.seed = seed

    def get_m_rate(self):
        return self.m_rate

    def set_m_rate(self, m_rate):
        self.m_rate = m_rate
        self.blocks_multiply_const_vxx_0.set_k((self.m_rate, ))

    def get_if_rate(self):
        return self.if_rate

    def set_if_rate(self, if_rate):
        self.if_rate = if_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.if_rate)
        self.channels_fading_model_0.set_fDTs(self.dpp/self.if_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-8e3, self.fc+8e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.if_rate)

    def get_gauss(self):
        return self.gauss

    def set_gauss(self, gauss):
        self.gauss = gauss

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.band_pass_filter_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-8e3, self.fc+8e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_frequency(self.fc)

    def get_dpp(self):
        return self.dpp

    def set_dpp(self, dpp):
        self.dpp = dpp
        self.channels_fading_model_0.set_fDTs(self.dpp/self.if_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

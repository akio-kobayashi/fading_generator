#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Feb  2 13:43:17 2020
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=10,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 10, 10, firdes.WIN_HAMMING, 6.76))
        self.channels_fading_model_0 = channels.fading_model( 8, 4e-1/960e3, True, 1, 256 )
        self.carrier = analog.sig_source_f(samp_rate*20, analog.GR_COS_WAVE, 150000, 1, 0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/akio/chop_sample.wav', False)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('fading.wav', 1, samp_rate, 16)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/3,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((4, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((500e-3, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((1, ))
        self.band_pass_filter_0 = filter.fir_filter_ccf(2, firdes.band_pass(
        	1, samp_rate*20, 120e3, 180e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.analog_am_demod_cf_0_0 = analog.am_demod_cf(
        	channel_rate=samp_rate*10,
        	audio_decim=10,
        	audio_pass=4000,
        	audio_stop=6000,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_am_demod_cf_0_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.analog_am_demod_cf_0_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.carrier, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.channels_fading_model_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_add_const_vxx_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 10, 10, firdes.WIN_HAMMING, 6.76))
        self.carrier.set_sampling_freq(self.samp_rate*20)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/3)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate*20, 120e3, 180e3, 2e3, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar 17 17:45:49 2020
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
import argparse

file1='/media/akio/ssd1/fading_generator/long2.wav'
file2='/media/akio/ssd1/fading_generator/fading+gauss2.raw'
file3='/media/akio/ssd1/fading_generator/gauss_noise_only2.raw'
file4='/media/akio/ssd1/fading_generator/original2.raw'
file5='/media/akio/ssd1/fading_generator/fading2.raw'
file6='/media/akio/ssd1/fading_generator/gauss_noise2.raw'
file7='/media/akio/ssd1/fading_generator/carrier_fading2.raw'
file8='/media/akio/ssd1/fading_generator/carrier_fading+gauss2.raw'

class top_block(gr.top_block):

    def __init__(self, args):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.seed = seed = args.seed
        self.m_rate = m_rate = args.m_rate
        self.if_rate = if_rate = samp_rate*40
        self.gauss = gauss = args.gauss
        self.fc = fc = args.fc
        self.dpp = dpp = args.dop
        self.sinu = sinu = args.sinu
        
        ##################################################
        # Blocks
        ##################################################
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
        self.low_pass_filter_1_0 = filter.fir_filter_fff(40, firdes.low_pass(
        	1, if_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(40, firdes.low_pass(
        	1, if_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(301, firdes.WIN_HAMMING, 6.76)
        self.high_pass_filter_0_1 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0_0_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.channels_fading_model_0 = channels.fading_model(sinu, dpp/if_rate, True, 2, 256 )
        self.blocks_wavfile_source_0 = blocks.wavfile_source(file1, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((m_rate, ))
        self.blocks_file_sink_0_5 = blocks.file_sink(gr.sizeof_float*1, file2, False)
        self.blocks_file_sink_0_5.set_unbuffered(False)
        self.blocks_file_sink_0_4 = blocks.file_sink(gr.sizeof_float*1, file3, False)
        self.blocks_file_sink_0_4.set_unbuffered(False)
        self.blocks_file_sink_0_3 = blocks.file_sink(gr.sizeof_float*1, file4, False)
        self.blocks_file_sink_0_3.set_unbuffered(False)
        self.blocks_file_sink_0_2 = blocks.file_sink(gr.sizeof_float*1, file5, False)
        self.blocks_file_sink_0_2.set_unbuffered(False)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_float*1, file6, False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, file7, False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, file8, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.band_pass_filter_0_1 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-7.5e3, fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-7.5e3, fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-7.5e3, fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-7.5e3, fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	4, if_rate, fc-7.5e3, fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0 = analog.sig_source_f(if_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, gauss, seed, 8192)
        self.analog_am_demod_cf_0_1 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )
        self.analog_am_demod_cf_0_0_0_0 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )
        self.analog_am_demod_cf_0_0_0 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )
        self.analog_am_demod_cf_0_0 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=fc,
        	audio_decim=40,
        	audio_pass=7500,
        	audio_stop=10e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_am_demod_cf_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.analog_am_demod_cf_0_0, 0), (self.high_pass_filter_0_0, 0))
        self.connect((self.analog_am_demod_cf_0_0_0, 0), (self.high_pass_filter_0_0_0, 0))
        self.connect((self.analog_am_demod_cf_0_0_0_0, 0), (self.high_pass_filter_0_0_0_0, 0))
        self.connect((self.analog_am_demod_cf_0_1, 0), (self.high_pass_filter_0_1, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.analog_am_demod_cf_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.analog_am_demod_cf_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.analog_am_demod_cf_0_0_0_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.analog_am_demod_cf_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.band_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.channels_fading_model_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_file_sink_0_5, 0))
        self.connect((self.high_pass_filter_0_0, 0), (self.blocks_file_sink_0_3, 0))
        self.connect((self.high_pass_filter_0_0_0, 0), (self.blocks_file_sink_0_2, 0))
        self.connect((self.high_pass_filter_0_0_0_0, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.high_pass_filter_0_1, 0), (self.blocks_file_sink_0_4, 0))
        self.connect((self.hilbert_fc_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.low_pass_filter_1_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.low_pass_filter_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_if_rate(self.samp_rate*40)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_1.set_taps(firdes.high_pass(1, self.samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0_0_0.set_taps(firdes.high_pass(1, self.samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0_0.set_taps(firdes.high_pass(1, self.samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(1, self.samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 50, 10, firdes.WIN_HAMMING, 6.76))
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
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.if_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.if_rate, 7500, 100, firdes.WIN_HAMMING, 6.76))
        self.channels_fading_model_0.set_fDTs(self.dpp/self.if_rate)
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.if_rate)

    def get_gauss(self):
        return self.gauss

    def set_gauss(self, gauss):
        self.gauss = gauss
        self.analog_fastnoise_source_x_0.set_amplitude(self.gauss)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(4, self.if_rate, self.fc-7.5e3, self.fc+7.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_frequency(self.fc)

    def get_dpp(self):
        return self.dpp

    def set_dpp(self, dpp):
        self.dpp = dpp
        self.channels_fading_model_0.set_fDTs(self.dpp)


def main(top_block_cls=top_block, options=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--gauss', type=float, default=1.0)
    parser.add_argument('--seed', type=int, default=128)
    parser.add_argument('--dop', type=float, default=10.0)
    parser.add_argument('--fc', type=int, default=594e3)
    parser.add_argument('--m-rate', type=float, default=0.8)
    parser.add_argument('--sinu', type=int, default=8)
    
    args=parser.parse_args()
    
    tb = top_block_cls(args)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()

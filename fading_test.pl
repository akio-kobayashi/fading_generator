#!/usr/bin/perl
use strict;
use Math::Random::MT qw/rand srand/;
    
my $file="/run/user/1000/gvfs/smb-share:server=asr00nas.local,share=home/data/jnas/JNAS_3/WAVES_DT/MP05/NP/NMP05160_DT.wav";
# 0.01 dpp < 1.00?
my $dop=$ARGV[0];
#my $file = $_;
$file =~ /([^\/]+)\.wav/;
my $speech_tag = $1;
my $line = `soxi $file | grep samples`;
if ($line =~ /\s+(\d+)\s+samples/g){
    my $samples = $1;
    my $long = "long.wav";
    system "sox gauss.wav $file $long";

    #my $seed = int(rand(2**10));
    #my $dop = (rand(2)-1.0)+1.0;
    #my $gauss = rand(1)/20.0;
    my $fc = 594e3;

    my $script="fading_b.py";
    my $seed=0;
    my $gauss=0.1;
    system "python fading_b.py --dop $dop --seed $seed --gauss $gauss --fc $fc";
    my $dir = "temp/".$speech_tag;
    system "mkdir -p $dir";

    my $orig_rate = 48000;
    my $conv_rate = 16000;
    my $original="original.raw";
    my $fading="fading.raw";
    my $fading_gauss="fading+gauss.raw";
    my $gauss_noise="gauss_noise.raw";
    my $gauss_noise_only="gauss_noise_only.raw";
    my $carrier_fading="carrier_fading.raw";
    my $carrier_fading_gauss="carrier_fading+gauss.raw";

    $line = `sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $original -n stat 3>&2 2>&1 1>&3|head -1`;
    chomp($line);
    $line =~/(\d+)$/; my $lsamples = $1;
    print $lsamples;
    my $remain = $lsamples - $samples*3;

    print "$speech_tag $seed $dop $gauss $lsamples $samples $remain\n";
    print OUT "$speech_tag $seed $dop $gauss $lsamples $samples $remain\n";
	
    $remain = $remain."s";
    system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $original -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/original_16k.raw trim $remain";
    system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $fading -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/fading_16k.raw trim $remain";
    system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $fading_gauss -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/fading+gauss_16k.raw trim $remain";
    system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $gauss_noise -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/gauss_noise_16k.raw trim $remain";
    system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $gauss_noise_only -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/gauss_noise_only_16k.raw trim $remain";
    system "cp -f $carrier_fading $dir/";
    system "cp -f $carrier_fading_gauss $dir/";
}

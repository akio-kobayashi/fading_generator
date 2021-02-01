#!/usr/bin/perl
use strict;
use Math::Random::MT qw/rand srand/;

my $rate=16000;
my $opt1="-c 1 --endian little -b 32 -e float -t raw -r $rate";
my $opt2="-c 1 --endian little -b 16 -t wav -r $rate";

srand(time^$$);

my $mod=$ARGV[0];
my $out=">./data_fading.".$mod.".list";
open(OUT, $out);

my $num = 0;

while(<STDIN>){
    if ($num % 4 != $mod){
	++$num;
	next;
    }
    ++$num;

    chomp;
    my $file = $_;
    $file =~ /([^\/]+)\.wav/;
    my $speech_tag = $1;
    my $line = `soxi $_ | grep samples`;
    if ($line =~ /\s+(\d+)\s+samples/g){
	my $samples = $1;
	my $long = "long".$mod.".wav";
	system "sox gauss.wav $file $long";

	my $seed = int(rand(2**10));
	#my $dop = (rand(2)-1.0)+1.0;
	#my $dop = (rand(5)-1.0)+1.0;
	my $dop = 1+rand(2);
	my $sinu = 1+int(rand(7));
	#my $gauss = rand(1)/20.0;
	#my $gauss = rand(10)/20.0;
	my $gauss = 0.5+rand(10)/20.0;
	my $fc = 594e3;

	my $script="fading_b".$mod.".py";
	system "python -u $script --dop $dop --seed $seed --gauss $gauss --fc $fc --sinu $sinu";
	my $dir = "/media/akio/hdd1/fading_generator/fading_data2/".$speech_tag;
	system "mkdir -p $dir";

	my $orig_rate = 48000;
	my $conv_rate = 16000;
	my $original="original".$mod.".raw";
	my $fading="fading".$mod.".raw";
	my $fading_gauss="fading+gauss".$mod.".raw";
	my $gauss_noise="gauss_noise".$mod.".raw";
	my $gauss_noise_only="gauss_noise_only".$mod.".raw";
	my $carrier_fading="carrier_fading".$mod.".raw";
	my $carrier_fading_gauss="carrier_fading+gauss".$mod.".raw";
	
	$line = `sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $original -n stat 3>&2 2>&1 1>&3|head -1`;
	chomp($line);
	$line =~/(\d+)$/; my $lsamples = $1;
	my $remain = $lsamples - $samples*3;

	print "$speech_tag $seed $dop $gauss $lsamples $samples $remain $sinu\n";
	print OUT "$speech_tag $seed $dop $gauss $lsamples $samples $remain $sinu\n";
	
	$remain = $remain."s";
	system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $original -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/original_16k.raw trim $remain";
	system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $fading -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/fading_16k.raw trim $remain";
	system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $fading_gauss -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/fading+gauss_16k.raw trim $remain";
	system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $gauss_noise -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/gauss_noise_16k.raw trim $remain";
	system "sox -c 1 --endian little -b 32 -e float -t raw -r $orig_rate $gauss_noise_only -c 1 --endian little -b 32 -e float -t raw -r $conv_rate $dir/gauss_noise_only_16k.raw trim $remain";
	system "cp -f $carrier_fading $dir/";
	system "cp -f $carrier_fading_gauss $dir/";

	system "sox $opt1 $dir/original_16k.raw $opt2 $dir/original_16k.wav";
	system "sox $opt1 $dir/fading_16k.raw $opt2 $dir/fading_16k.wav";
	system "sox $opt1 $dir/gauss_noise_only_16k.raw $opt2 $dir/gauss_noise_only_16k.wav";
	system "sox $opt1 $dir/fading+gauss_16k.raw $opt2 $dir/fading+gauss_16k.wav";

    }
}

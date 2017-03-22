#!/usr/bin/perl -w

use strict;
use warnings;

my $ftp_range_low = 30000;
my $ftp_range_high = 39999;
my $c_type = "ftp";

if ($c_type eq "ftp" || $c_type eq "export") {
	open (PASSWD, "/GitHub/users/mallikbheesetti/testrepo1/passwd") || die "Unable to open file!\n";
	my %uids;
	my $uid;
	while (<PASSWD>) {
		my @tmp = split /:/;
		$uids{$tmp[2]}++;
	}
	my @uidkeys = keys %uids;
	my @uidvals = values %uids;

#	print "@uidkeys[0..$#uidkeys]\n";
#	print "@uidvals[0..$#uidvals]\n";
#	print "@tmp[0..$#tmp]\n";

	for ($ftp_range_low..$ftp_range_high) {
		$uid = $_ ;
		print "$uid\t:\t$_\n";
#		print "$uids{$uid}\n";
#		last if ($uids{$uid} == "");
#		print "$uids{$uid}\n";
	}
}

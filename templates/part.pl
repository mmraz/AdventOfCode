#!/usr/bin/env perl

my @inputs;
my $DEBUG = 0;

open(FIN, "<input");
while(<FIN>) {
    chomp;
    push @inputs,  $_;
}
close(FIN);

print "";

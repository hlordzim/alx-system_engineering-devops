#!/usr/bin/env bash
# Using Puppet to make changes to our configuration file.

file { 'etc/ssh_config':
	ensure => present,
	mode    => '0644',

content => "

	#SSH Client Configuration
	host"
	IdentityFile ~/.ssh/school
	PasswordAuthentication no

	",
}

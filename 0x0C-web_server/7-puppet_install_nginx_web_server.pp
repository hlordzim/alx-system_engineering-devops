# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

file_line { 'add redirect rule':
    path    => '/etc/nginx/sites-available/default',
    line    => '    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    match   => '^    # Other configuration lines',
    require => Package['nginx'],
    notify  => Service['nginx']
}

service {'nginx':
    ensure => running,
    require => Package['nginx']
}

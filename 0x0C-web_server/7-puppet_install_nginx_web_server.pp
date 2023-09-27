# nginx_setup.pp file with puppet


# ensure the necessary packages and repositories are managed
class { 'nginx':
  manage_repo   => true,
  package_ensure => 'latest',
}


# set up the default nginx virtual host
nginx::resource::server { 'default_server':
  listen_options => 'default_server',
  listen_port    => 80,
  www_root       => '/var/www/html',
  index_files    => ['index.html'],
}


# set up redirect for /redirect_me
nginx::resource::location { 'redirect_me':
  location       => '/redirect_me',
  server         => 'default_server',
  redirect       => 'http://$host/',
  http_ensure    => '301',
}


# create the root index.html with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<h1>Hello World!</h1>',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Class['nginx'],
}

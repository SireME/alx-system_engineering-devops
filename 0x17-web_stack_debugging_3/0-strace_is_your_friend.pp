# 0-strace_is_your_friend.pp

# Define an Apache site resource to configure the virtual host.
file { '/etc/apache2/sites-available/your_site.conf':
  ensure  => present,
  content => "
    <VirtualHost *:80>
        ServerName your_server_name
        DocumentRoot /var/www/your_document_root
        # Add your configuration directives here
    </VirtualHost>
  ",
}

# Ensure the virtual host configuration file is enabled.
# # note : your_site is a placeholder
apache::vhost { 'your_site':
  vhost_name    => 'your_server_name',
  docroot       => '/var/www/your_document_root',
  priority      => 10,
  override      => 'All',
  vhost_aliases => [],
}


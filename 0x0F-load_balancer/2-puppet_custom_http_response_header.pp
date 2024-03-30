# Puppet manifest to setup up an ubuntu server
# Update nginx, and custom http headers

exec { 'update system':
  command => '/usr/bin apt-get -y update',
  provider  => 'shell'
}

# Update ngnix
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

# Change content of index file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  owner => 'ubuntu',
  group => 'ubuntu',
  mode  => '7624'
}

# Redirect_me
exec { 'redirect_me':
  command => 'sed -i \'^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=xZIwIoekjgw;}\' /etc/nginx/sites-available/default',
  provider  => 'shell',
}

# Custom HTTP HEADER
exec { 'custom HTTP HEADER':
  command => 'sed -i "0,/location \/ {/s/location \/ {/&\n\t\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default',
  provider  => 'shell',
}

# Restart ngnix
service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
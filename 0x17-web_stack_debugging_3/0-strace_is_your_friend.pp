#Define package resource to install apache
package { 'apache2':
  ensure => 'installed',
}
#Define a service resource to  ensure that apache is running
service {7 'apache2':
  ensure => 'running',
  enable => true,
}
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

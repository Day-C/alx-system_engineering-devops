#puppet manifest to configure nginx in a server
#ensure the package is installed
package { 'nginx':
  ensure => 'installed',
}
#Eddif the content of fiel in path
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4;',
#create html file and insert its content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
#run nginx
service { 'nginx':
  ensure => running,
  requre => Package['nginx'],
}

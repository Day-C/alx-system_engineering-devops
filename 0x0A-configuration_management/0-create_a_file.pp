#create a file and give it permissions,an owner, group and write content in it
file { '/temp/school':
  path    => '/temp/school',
  content => 'i love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}

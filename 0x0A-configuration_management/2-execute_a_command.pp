#execuke a pkill command  to stpo a process
exec { 'pkill':
command => 'pkill -9 -f killmenow',
path    => ['/usr/bin', 'usr/sbin', '/bin']
}

# too many open files/ulimit 15
exec { 'ulimit change':
  command => "sed -i 's/15/4096/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

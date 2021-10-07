# su - holberton too many open files
# http://woshub.com/too-many-open-files-error-linux/

exec { 'hard limit increase':
  command => 'sed -i "/holberton hard/s/5/97816/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft limit increase':
  command => 'sed -i "/holberton soft/s/4/97816/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

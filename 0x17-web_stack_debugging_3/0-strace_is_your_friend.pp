# Fix 500 error on apache. Type phpp instead of php
exec { 'wordpress fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

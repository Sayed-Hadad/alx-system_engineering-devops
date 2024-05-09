# Fixes the typo found in php  file that causes the server error

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/:/usr/bin/:/usr/sbin/:/sbin/'
}

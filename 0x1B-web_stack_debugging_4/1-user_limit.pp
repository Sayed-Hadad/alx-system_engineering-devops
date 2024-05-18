# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

exec { 'change hard_settings':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1000/' /etc/security/limits.conf",
  path    => '/bin/:/usr/local/bin'
}

exec { 'change soft_settings':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1000/' /etc/security/limits.conf",
  path    => '/bin/:/usr/local/bin'
}

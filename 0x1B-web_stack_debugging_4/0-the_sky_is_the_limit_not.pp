#change the ulimit to allow more requests to come to the server

exec { 'fix_nginx':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => '/bin/:/usr/local/bin'
}
exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}

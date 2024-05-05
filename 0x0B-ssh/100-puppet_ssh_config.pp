# using puppet to set up the client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "
      Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  "
}

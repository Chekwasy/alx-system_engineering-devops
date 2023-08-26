# killmenow
exec { 'killmenow':
  path    => [ '/usr/local/sbin', '/usr/sbin', '/usr/bin', '/sbin', '/bin' ],
  command => 'pkill killmenow',
  provider => 'shell',
  }

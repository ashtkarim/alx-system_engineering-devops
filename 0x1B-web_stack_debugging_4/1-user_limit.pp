# Enable the user holberton to login and open files without error.

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/60000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/60000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

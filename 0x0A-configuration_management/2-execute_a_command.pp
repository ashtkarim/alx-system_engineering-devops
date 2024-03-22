#Create a manifest that kills a process named killmenow using Puppet
exec { 'pkill':
    command => 'pkill killmenow',
    path    => ['/bin', '/usr/bin'],
    returns => [0, 1],
}
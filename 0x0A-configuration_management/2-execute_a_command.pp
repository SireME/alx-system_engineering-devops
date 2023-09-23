# create manifest that kill process named killnow

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}

# 1-user_limit.pp

user { 'holberton':
  ensure     => 'present',
  managehome => true,
}

# Set file limits for the holberton user
limits { 'holberton':
  ensure     => 'present',
  limit_type => 'soft',
  limit_item => 'nofile',
  value      => 65536,
}

limits { 'holberton':
  ensure     => 'present',
  limit_type => 'hard',
  limit_item => 'nofile',
  value      => 65536,
}


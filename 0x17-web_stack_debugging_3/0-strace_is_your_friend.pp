/*
  This puppet manifest sets up an apache server  and 
  fiexes an error in one of its files that is causing an thhp 500 error
*/

package { 'apache2':
  ensure  => 'installed',
}

#running the process  of not alrady
service { 'apache2':
  ensure  => 'running',
  enable  => true,
}

#correct the error in the file using the sed command
exec { 'replace_faulty_pattern_in_file':
  command  => "/bin/sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' wp-settings.php",
  onlyif   => "/bin/grep -q 'class-wp-locale.phpp' wp-settings.php",
  cwd      => '/var/www/html',
}

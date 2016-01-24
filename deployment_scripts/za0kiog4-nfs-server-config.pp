notice('MODULAR: za0kiog4-nfs-server-config.pp')

$za0kiog4 = hiera('za0kiog4', {})
$export = pick($za0kiog4['export'], '/var/lib/za0kiog4')
$clients = pick($za0kiog4['clients'], '10.20.0.0/24(rw,insecure,async,no_root_squash)')

class { '::nfs':
   server_enabled => true
 }

 nfs::server::export{ $export:
   ensure  => 'mounted',
   clients => $clients
}

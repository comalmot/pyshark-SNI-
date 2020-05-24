capture = pyshark.LiveCapture(interface='eth0', display_filter="tcp.port==443 && ssl.handshake.type == 1")
capture.sniff(timeout=1)
sni = capture[n].ssl.handshake_extensions_server_name



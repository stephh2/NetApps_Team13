from zeroconf import ServiceInfo, Zeroconf, ZeroConfServiceRegistration, NonUniqueNameException

def register_service(self, service_type, service_name, port=None, description=None):
        if description is None:
            description = {}
        if port is None:
            port = ZeroConfServiceRegistration._get_unique_port()
        hostname = ZeroConfServiceRegistration._get_hostname()
        network_interface_list = ZeroConfServiceRegistration._get_network_interfaces()
        for interface_name, ip_address in network_interface_list:
            info = None
            for index in range(0, 9999):
                name_candidate = service_name if index == 0 else "{} ({})".format(service_name, index)
                info = ServiceInfo(service_type.value,
                                   name_candidate + "." + service_type.value,
                                   socket.inet_aton(ip_address), port, 0, 0,
                                   description, hostname)
                try:
                    self._zeroconf.register_service(info)
                except NonUniqueNameException:
                    print("Service name is used:", name_candidate + "." + service_type.value)
                else:
                    break
            self._service_list.append((service_type, service_name, ip_address, port, info))
        return port
    
    
    
if __name__ == "__main__":
    service_type = ZeroConfServiceRegistration.ServiceType.HTTP
    register_service(service_type, "Team_13")
    
    
    
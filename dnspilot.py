import config
from re import match


class Dns:
    def __init__(self, dns_title, nameservers):
        self.dns_title = dns_title
        self.nameservers = nameservers

    @property
    def dns_title(self):
        return self.__dns_title

    @dns_title.setter
    def dns_title(self, title):
        if type(title) == type(str()):
            self.__dns_title = title  # TODO: Adding a duplicate title checking system
        else:    
            raise ValueError("DNS object only takes str.")

    @property
    def nameservers(self):
        return self.__nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        #ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|
        if type(nameservers) in [type(list()), type(tuple()), type(set())]:
            if len(nameservers) == 2:
                #if match(ValidIpAddressRegex, nameservers[0]) and match(ValidIpAddressRegex, nameservers[1]):
                self.__nameservers = nameservers
                #else:
                    #raise ValueError(
                        #"invalid nameserves structure. please set in this format ('0.0.0.0','0.0.0.0')")
            else:
                raise ValueError(
                    "nameservers of DNS object only take a itreble with len 2")
        else:
            raise ValueError(
                "nameservers of DNS object only takes list,tuple and set")

    def chenge_dns(self):
        try:
            with open(config.RESOLVCONF_PATH, "w") as resolv_config:
                nameserver1 = self.nameservers[0]
                nameserver2 = self.nameservers[1]
                resolv_config.write(
                    f"nameserver {nameserver1}\nnameserver {nameserver2}\n")
                resolv_config.close()
        except PermissionError as e:
            raise PermissionError("run dns chenger with sudo command")


if __name__ == "__main__":
    M = Dns("google", ("178.22.122.100", "185.51.200.2"))
    M.chenge_dns()
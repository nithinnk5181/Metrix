import configparser

config=configparser.RawConfigParser()
config.read("Admin/Configurations/config.ini")



class ReadConfig():
    @staticmethod
    def getBaseuRL():
        URL=config.get('common info','ADMIN_BASEURL')
        return URL

    @staticmethod
    def getUsername():
        Username=config.get('common info','ADMIN_USERNAME')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'ADMIN_PASSWORD')
        return Password




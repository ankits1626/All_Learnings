class BaseLocator:
    def __init__(self, platform):
        self.android = None
        self.iOS = None
        self.platform = platform
        self.param = None
        self.initialize_locators()

    def initialize_locators(self):
        raise NotImplementedError("Subclasses must implement initialize_locators method")

    def get_locator(self, key):
        if self.platform == 'iOS':
            return self.iOS.get(key)
        elif self.platform == 'Android':
            return self.android.get(key)
        else:
            raise ValueError("Invalid platform provided")
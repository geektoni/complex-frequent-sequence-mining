import configparser

class ExperimentParser:

    def __init__(self, args, config_path):
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)
        self.args = args

    def parse(self):

        self.args["algorithms"] = self.getlist(self.parser["Default"]["algorithms"])
        self.args["jaccard_tresh"] = self.getlist(self.parser["Default"]["jaccard_tresh"])
        self.args["database_size"] = self.getlist(self.parser["Default"]["database_size"])
        self.args["max_tree_size"] = self.getlist(self.parser["Default"]["max_tree_size"])
        self.args["max_sequence_size"] = self.getlist(self.parser["Default"]["max_sequence_size"])
        self.args["min_support"] = self.getlist(self.parser["Default"]["min_support"])

        return self.args


    def getlist(self, option, sep=',', chars=None):
        """Return a list from a ConfigParser option. By default,
           split on a comma and strip whitespaces."""
        return [chunk.strip(chars) for chunk in option.split(sep)]



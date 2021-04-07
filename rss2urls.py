"""
Convert a yaml file "rss.yml" containing RSS feeds to a newsboat
supported "urls"
"""
import os
import sys
import yaml


class urlsRSS:
    """
    Parameters
    ----------
    ymlfile : str
        A yaml file containing the rss links and metadata

    urlfile : str
        A file to dump the contents
    """
    def __init__(self, ymlfile: str, urlfile: str) -> None:
        self.ymlfile = ymlfile
        self.urlfile = urlfile
        self.loadRSS()

    def loadRSS(self) -> None:
        """
        load the yaml file into a python dictionary
        """
        with open(self.ymlfile, 'r') as f:
            self.content = yaml.load(f, yaml.FullLoader)

    def dumpRSS(self) -> None:
        """
        Dumps the contents to a file
        """
        with open(self.urlfile, 'w') as g:
            g.write("###############################################\n")
            g.write("# RSS FEEDS\n")
            g.write("###############################################\n\n")
            for key, value in self.content.items():
                if value['type'] == 'general':
                    g.write('{} "~FEED: {}"\n'.format(key, value['name']))

                elif value['type'] == 'youtube':
                    line1 = "https://www.youtube.com/feeds/videos.xml?channel_id={}".format(key)
                    line2 = '{} "~YOUTUBE: {}"\n'.format(line1, value['name'])
                    g.write(line2)

                elif value['type'] == 'reddit':
                    line1 = "https://www.reddit.com/r/{}.rss".format(key)
                    line2 = '{} "~REDDIT: {}"\n'.format(line1, value['name'])
                    g.write(line2)

                elif value['type'] == 'github':
                    line1 = "https://www.github.com/{}.atom".format(key)
                    line2 = '{} "~GITHUB: {}"\n'.format(line1, value['name'])
                    g.write(line2)

                elif value['type'] == 'gitlab':
                    line1 = "https://www.gitlab.com/{}.atom".format(key)
                    line2 = '{} "~GITLAB: {}"\n'.format(line1, value['name'])
                    g.write(line2)

                elif value['type'] == 'sourceforge':
                    line1 = "https://www.sourceforge.net/p/{}/activity/feed".format(key)
                    line2 = '{} "~SOURCEFORGE: {}"\n'.format(line1, value['name'])
                    g.write(line2)



def main():
    """
    main file
    """
    urlfile = 'urls'
    a = urlsRSS(yml_file, urlfile)
    a.dumpRSS()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        yml_file = "./rss.yml"
        yml_file = os.path.join(os.environ['HOME'], ".newsboat/rss.yml")
    elif len(sys.argv) == 2:
        yml_file = sys.argv[1]
    else:
        print("Invalid number of arguments")
        sys.exit(1)
    main()

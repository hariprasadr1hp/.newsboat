
import os
import sys
import yaml


def loadRSSdata(yml_file):
    with open(yml_file, 'r') as f:
        content = yaml.load(f, yaml.FullLoader)
    return content

def dump2URLS(urlfile, content):
    with open(urlfile, 'w') as g:
        newsfeeds   = content['newsfeeds']
        youtube     = content['youtube']
        reddit      = content['reddit']
        # github      = content['github']
        # gitlab      = content['gitlab']
        # bitbucket   = content['bitbucket']

        g.write("################################################\n")
        g.write("# NEWSFEEDS\n")
        g.write("################################################\n")
        g.write("\n")
        for link, title in newsfeeds.items():
            g.write('{} "~FEED: {}"\n'.format(link,title))
        g.write("\n")
        g.write("################################################\n")
        g.write("# YOUTUBE\n")
        g.write("################################################\n")
        g.write("\n")
        for link, title in youtube.items():
            g.write('https://www.youtube.com/feeds/videos.xml?channel_id={} "~YOUTUBE: {}"\n'.format(link,title))
        g.write("\n")
        g.write("################################################\n")
        g.write("# REDDIT\n")
        g.write("################################################\n")
        g.write("\n")
        for feed in reddit:
            g.write('https://www.reddit.com/r/{}.rss "~REDDIT: {}"\n'.format(feed,feed))
        g.write("\n")
        g.write("################################################\n")
        g.write("# GITHUB\n")
        g.write("################################################\n")
        g.write("\n")
        # for feed in reddit:
        #     g.write('https://www.reddit.com/r/{}.rss "~REDDIT: {}"\n'.format(feed,feed))
        g.write("\n")
        g.write("################################################\n")
        g.write("# GITLAB\n")
        g.write("################################################\n")
        g.write("\n")
        # for feed in reddit:
        #     g.write('https://www.reddit.com/r/{}.rss "~REDDIT: {}"\n'.format(feed,feed))
        g.write("\n")
        g.write("################################################\n")
        g.write("# BITBUCKET\n")
        g.write("################################################\n")
        g.write("\n")
        # for feed in reddit:
        #     g.write('https://www.reddit.com/r/{}.rss "~REDDIT: {}"\n'.format(feed,feed))
        g.write("\n")


def main(yml_file):
    content = loadRSSdata(yml_file)
    urlfile = 'urls'
    dump2URLS(urlfile, content)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        yml_file = os.path.join(os.environ['HOME'],'.newsboat/rss.yml')
    elif len(sys.argv) == 2:
        yml_file = sys.argv[1]    
    else:
        print("Invalid number of arguments")
        exit(1)
    main(yml_file)

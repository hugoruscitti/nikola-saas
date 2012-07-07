import ConfigParser, os

def get_url_from_repository(repo_path):
    import configdict
    cf = configdict.ConfigDict(os.path.join(repo_path, '.git/config'))
    return cf['remote "origin"']['url']

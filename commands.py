import subprocess

def clonar_repositorio(url, directorio):
    print "ejecutando clone sobre %s" %(url)
    p = subprocess.Popen(['rm', '-rf', directorio])
    p.wait()

    p = subprocess.Popen(['git', 'clone', '--progress', url, directorio], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    error_code = p.wait()

    if error_code:
        raise Exception(error_code)

    return p.communicate()[0]



if __name__ == "__main__":
    print clonar_repositorio("https://github.com/kennethreitz/envoy.git", "/tmp/site")

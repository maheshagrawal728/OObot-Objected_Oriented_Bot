import githubWrapper
import cacheit
import zipfile
import subprocess
import os
import json

# downloads the zipfile and extract it to the OOBOT temp directory
def downloadzipfile(templateName, link, repoName):
    proc = subprocess.Popen("wget --no-check-certificate " + link, cwd='../OOBOT', stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if "failed" in str(err) or "ERROR" in str(err):
        print err
        return
    zip_ref = zipfile.ZipFile('../OOBOT/master.zip', 'r')
    zip_ref.extractall('../OOBOT')
    zip_ref.close()
    os.remove('../OOBOT/master.zip')
    os.rename('../OOBOT/' + repoName + '-master', '../OOBOT/' + templateName)

# user can upload the template they have in their public github to the OOBOT data store
def UseCase2(templateName, lang, link):
    print templateName
    templateLang = templateName + '-' + lang
    returnvalue = githubWrapper.createRepo(templateLang)
    if (returnvalue == -1):
        return -1
    repoName = link[link.rfind('/') + 1:]
    link = link + "/archive/master.zip"
    downloadzipfile(templateLang, link, repoName)
    cacheit.data["localpaths"][templateLang] = "../OOBOT/" + templateLang + "/"
    print cacheit.data["localpaths"]
    githubWrapper.pushRepoSelf(templateLang, cacheit.data["localpaths"][templateLang])
    return 1

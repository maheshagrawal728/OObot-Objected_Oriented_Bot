import requests
import json
import os
import base64
import tarfile
import shutil
import sys

token = "token " + os.environ['GITHUBTOKEN']
headers = {"User-Agent": "EnableIssues",
           "content-type": "application/json",
           "Authorization": token}

urlRoot = "https://github.ncsu.edu/api/v3"

# downloads the tar file from the specified url
def downloadtarball(local_filename, repoName):
    getContentUrl = urlRoot + '/repos/' + 'OOBOT' + '/' + repoName + '/tarball' + '/' + 'master'
    try:
        r = requests.get(getContentUrl, headers=headers, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    except:
        print sys.exc_info()

# downloads the zip file from the specified url
def downloadzipball(local_filename, repoName):
    getContentUrl = urlRoot + '/repos/' + repoName + '/zipball' + '/' + 'master'
    try:
        r = requests.get(getContentUrl, headers=headers, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    except:
        print sys.exc_info()

# extracts the tar file to the destination directory i.e., temp directory named OOBOT
def getContent(repoName):
    local_filename = repoName + '.tar.gz'
    downloadtarball(local_filename, repoName)
    try:
        tar = tarfile.open(local_filename, mode='r:gz')
        tar.extractall('../OOBOT/' + repoName + 'TEMP')
        srcDir = '../OOBOT/' + repoName + 'TEMP/' + os.listdir('../OOBOT/' + repoName + 'TEMP')[0]
        destDir = '../OOBOT/' + repoName + '/'
        # if the OOBOT directory already exists, then delete it
        if os.path.exists(destDir):
            shutil.rmtree(destDir)
        shutil.copytree(srcDir, destDir)
        tar.close()
        os.remove(local_filename)
        shutil.rmtree('../OOBOT/' + repoName + 'TEMP/')
    except:
        os.remove(local_filename)
        print sys.exc_info()


'''
def getContent(userName, repoName):
    getContentUrl = urlRoot + '/repos/'+userName+'/'+repoName+'/tarball'+'/'+'master'
    command = 'curl -u username:' + os.environ['GITHUBTOKEN'] + ' -L ' + getContentUrl + ' > ' + repoName + '.tar.gz'
    print command
    proc = subprocess.Popen(command, cwd='../OOBOT', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    print out
    if "failed" in str(err) or "ERROR" in str(err):
        print str(err)
    proc = subprocess.Popen('tar zxvf ' + repoName + '.tar.gz ' + repoName, cwd='../OOBOT', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    print out
    if "failed" in str(err) or "ERROR" in str(err):
        print str(err)
'''

# fetches the list of repos that OOBOT has in its data store
def listOrganisationRepos(org):
    orgUrl = urlRoot + '/orgs/' + org + '/repos'
    r = requests.get(orgUrl, headers=headers)
    try:
        repoList = r.json()
    except:
        print "Could not access Organisation Repository" + 'org'
        return
    return repoList

def listRepos():
    listrepoUrl = urlRoot + '/user/repos'
    r = requests.get(listrepoUrl, headers=headers)
    try:
        allrepos = r.json()
    except:
        print "Could not access User Repository"
        return
    return allrepos

def getRepoUrl(userName, repoName):
    allrepos = listRepos()
    for eachrepo in allrepos:
        if userName + '/' + repoName not in eachrepo['full_name']:
            continue
        return str(eachrepo['html_url'])+"/tree/oobot"
    return ""

# create a branch in user's repo to push the template
def createBranch(userName, repoName):
    getBranchInfoUrl = urlRoot + '/repos/' + userName + '/' + repoName + '/git/refs/heads'
    try:
        r = requests.get(getBranchInfoUrl, headers=headers)
        responseJson = r.json()
    except:
        print "Could not get Branch Information"
        return

    try:
        for branches in responseJson:
            refSHA = branches['object']['sha']  # if  master branch is not present, use any sha to branch out
            if "master" in branches["ref"]:
                refSHA = branches['object']['sha']
                break
        data = {"ref": "refs/heads/oobot", "sha": refSHA}
        createBranchUrl = urlRoot + '/repos/' + userName + '/' + repoName + '/git/refs'
        r = requests.post(createBranchUrl, headers=headers, data=json.dumps(data))
        responseJson = r.json()
        # print response
        if "message" in responseJson.keys():
            print responseJson["message"]
            return -1
        return 0
    except:
        return -1

def getDownloadLink(userName, repoName):
    downloadLink = "https://github.ncsu.edu/" + userName + "/" + repoName + "/archive/master.zip"
    return downloadLink

# push the repo into the specified url
def pushRepo(userName, repoName, repoPath):
    for root, dirs, files in os.walk(repoPath):
        for file in files:
            if ".git" in root or ".gitignore" in root:
                continue
            filepath = os.path.join(root, file)
            pathInRepo = filepath.replace(repoPath, "")
            pushUrl = urlRoot + "/repos/" + userName + "/" + repoName + "/contents" + pathInRepo
            with open(filepath, 'r') as infile:
                content64 = base64.b64encode(infile.read())
            data = {"message": file, "content": str(content64), "branch": "oobot"}
            r = requests.put(pushUrl, headers=headers, data=json.dumps(data))
            if r is None:
                print "Push Repository Failed"

# use the github api to search the repo with specified language
def search(pattern, lang):
    searchUrl = 'https://api.github.com/search/repositories'
    parameters = 'q=' + pattern + '+language:' + lang + '&order=desc'
    searchHeaders = {"User-Agent": "EnableIssues",
                     "content-type": "application/json"}
    response = requests.get(searchUrl + '?' + parameters, headers=searchHeaders)
    res = ""
    if response.ok:
        print response.status_code
        jData = json.loads(response.content)
        print jData['total_count']
        # shows only the first 15 search results
        if (len(jData['items']) > 15):
            searchResults = jData['items'][:15]
        else:
            searchResults = jData['items']
        for dictx in searchResults:
            res += 'https://github.com/' + str(dictx['full_name']) + '\n'
        return res
    else:
        return None

def pushRepoSelf(repoName, repoPath):
    for root, dirs, files in os.walk(repoPath):
        for file in files:
            if ".git" in root:
                continue
            filepath = os.path.join(root, file)
            pathInRepo = filepath.replace(repoPath, "")
            pushUrl = urlRoot + "/repos/" + "OOBOT/" + repoName + "/contents/" + pathInRepo
            with open(filepath, 'r') as infile:
                content64 = base64.b64encode(infile.read())
            data = {"message": file, "content": str(content64), "branch": "master"}
            r = requests.put(pushUrl, headers=headers, data=json.dumps(data))
            try:
                print r.json()
            except:
                print "Push Repository Self Failed"


def createRepo(repoName):
    data = {"name": repoName, "private": False, "has_issues": True}
    createRepoUrl = urlRoot + '/orgs/' + 'OOBOT' + '/repos'
    try:
        r = requests.post(createRepoUrl, headers=headers, data=json.dumps(data))
        responseJson = r.json()
    except:
        print "create request failed"
        return
    if "message" in responseJson.keys():
        print responseJson["message"]
        return -1
    return 0

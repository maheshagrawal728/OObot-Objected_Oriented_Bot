import githubWrapper
import cacheit

"""
user can ask the OOBOT for a pattern it already has. Then they have an option to either download the template
or upload it to their ncsu github repo as a new branch
"""
def UseCase1(userName, repoName, patternName, lang):
    returnvalue = githubWrapper.createBranch(userName, repoName)
    if(returnvalue == -1):
        return -1
    githubWrapper.pushRepo(userName, repoName, cacheit.data["localpaths"][patternName+'-'+lang])
    return githubWrapper.getRepoUrl(userName, repoName)

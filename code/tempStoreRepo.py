import os
import githubWrapper
import cacheit

# clones existing repos from its data store to the temp directory named OOBOT
def cloneRepoFromDataStore():
    gitRepoNames = cacheit.getAvailPatterns()

    if not os.path.exists('../OOBOT'):
        os.makedirs('../OOBOT')

    print "Cloning existing patterns from OOBOT organization"
    for repoName in gitRepoNames:
        print "Cloning "+repoName
        githubWrapper.getContent(repoName)

import githubWrapper

# user can search the pattern template in public github
def UseCase3(templateName, prefLang):
	return githubWrapper.search(templateName, prefLang)